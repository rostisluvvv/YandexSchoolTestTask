f = open("inputs/input1.txt")

data_collection = f.readline()

count_data_centers, count_of_servers, event_count = map(int, data_collection.split(' '))


def data_collection_about_data_center(count_data_centers,
                                      count_of_servers,
                                      event_count):

    data_centers_of_active_server = [count_of_servers for _ in range(count_data_centers)]
    data_center_resets = [0 for _ in range(count_data_centers)]
    disabled_servers = [set() for _ in range(count_data_centers)]
    metrics = [0 for _ in range(count_data_centers)]
    min_data_center = 0
    max_data_center = 0

    for _ in range(event_count):
        line = f.readline()
        if 'DISABLE' in line:
            _, number_of_data_center, number_of_server = line.split(' ')
            number_of_data_center = int(number_of_data_center) - 1
            number_of_server = int(number_of_server) - 1

            if number_of_server not in disabled_servers[number_of_data_center]:
                data_centers_of_active_server[number_of_data_center] -= 1
                disabled_servers[number_of_data_center].add(number_of_server)
                metrics[number_of_data_center] = data_center_resets[
                              number_of_data_center] * data_centers_of_active_server[number_of_data_center]
            else:
                continue

            if max_data_center == number_of_data_center:
                max_data_center = max(range(count_data_centers),
                                      key=lambda number_of_data_center: metrics[number_of_data_center])
            if min_data_center != number_of_data_center:
                if metrics[min_data_center] > metrics[number_of_data_center]:
                    min_data_center = number_of_data_center
                elif metrics[min_data_center] == metrics[number_of_data_center]:
                    min_data_center = min(min_data_center, number_of_data_center)

        if 'RESET' in line:
            _, number_of_data_center = line.split(' ')
            number_of_data_center = int(number_of_data_center) - 1
            data_centers_of_active_server[number_of_data_center] = count_of_servers
            data_center_resets[number_of_data_center] += 1
            metrics[number_of_data_center] = data_center_resets[number_of_data_center] * count_of_servers
            disabled_servers[number_of_data_center] = set()

            if min_data_center == number_of_data_center:
                min_data_center = min(
                    range(count_data_centers),
                    key=lambda number_of_data_center: metrics[
                        number_of_data_center])
            if max_data_center != number_of_data_center:
                if metrics[max_data_center] < metrics[number_of_data_center]:
                    max_data_center = number_of_data_center
                elif metrics[max_data_center] == metrics[
                    number_of_data_center]:
                    max_data_center = min(max_data_center,
                                          number_of_data_center)

        if 'GETMAX' in line:
            print(max_data_center + 1)

        if 'GETMIN' in line:
            print(min_data_center + 1)


data_collection_about_data_center(count_data_centers, count_of_servers, event_count)
