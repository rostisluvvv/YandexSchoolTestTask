f = open("inputs/input3.txt")

data_collection = f.readline()

count_data_centers, count_of_servers, event_count = map(int, data_collection.split(' '))


def data_collection_about_data_center(count_data_centers,
                                      count_of_servers,
                                      event_count):

    data_centers_of_active_server = [count_of_servers for _ in range(count_data_centers)]

    data_center_resets = [0 for _ in range(count_data_centers)]

    state_server = [[1 for _ in range(count_of_servers)] for _ in range(count_data_centers)]

    for _ in range(event_count):
        line = f.readline()
        if 'DISABLE' in line:
            _, number_of_data_center, number_of_server = line.split(' ')
            number_of_data_center = int(number_of_data_center) - 1
            number_of_server = int(number_of_server) - 1
            if state_server[number_of_data_center][number_of_server]:
                data_centers_of_active_server[number_of_data_center] -= 1
                state_server[number_of_data_center][number_of_server] = 0

        if 'RESET' in line:
            _, number_of_data_center = line.split(' ')
            number_of_data_center = int(number_of_data_center) - 1
            data_centers_of_active_server[number_of_data_center] = count_of_servers
            data_center_resets[number_of_data_center] += 1
            state_server[number_of_data_center] = [1 for _ in range(count_of_servers)]

        if 'GETMAX' in line:
            max_data_center = max(
                range(count_data_centers),
                key=lambda number_of_data_center: data_centers_of_active_server[
                                                      number_of_data_center
                                                  ] * data_center_resets[number_of_data_center])
            print(max_data_center + 1)

        if 'GETMIN' in line:
            min_data_center = min(
                range(count_data_centers),
                key=lambda number_of_data_center: data_centers_of_active_server[
                                                      number_of_data_center
                                                  ] * data_center_resets[number_of_data_center])
            print(min_data_center + 1)

data_collection_about_data_center(count_data_centers, count_of_servers, event_count)