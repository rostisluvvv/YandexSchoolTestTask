f = open("input.txt")

data_collection = f.readline()

count_data_centers, count_of_servers, event_count = map(int, data_collection.split(' '))


def data_collection_about_data_center(count_data_centers,
                                      count_of_servers,
                                      event_count):
    data_centers_of_active_server = {num_data_center: count_of_servers
                                     for num_data_center in
                                     range(1, count_data_centers + 1)}

    data_center_resets = {
        num_data_center: 0 for num_data_center in range(
            1, count_data_centers + 1
        )
    }

    state_server = {
        num_data_center: {
            num_server: 1 for num_server in range(1, count_of_servers + 1)
        } for num_data_center in range(1, count_data_centers + 1)
    }

    for _ in range(event_count):
        line = f.readline()
        if 'DISABLE' in line:
            _, number_of_data_center, number_of_server = line.split(' ')
            number_of_data_center = int(number_of_data_center)
            number_of_server = int(number_of_server)
            if state_server[number_of_data_center][number_of_server]:
                data_centers_of_active_server[number_of_data_center] -= 1
                state_server[number_of_data_center][number_of_server] = 0

        if 'RESET' in line:
            _, number_of_data_center = line.split(' ')
            number_of_data_center = int(number_of_data_center)
            data_centers_of_active_server[number_of_data_center] = count_of_servers
            data_center_resets[number_of_data_center] += 1
            reset_dict = {num_server: 1 for num_server in range(
                1, count_of_servers + 1
            )}
            state_server[number_of_data_center] = reset_dict

        if 'GETMAX' in line:
            max_data_center = max(
                data_centers_of_active_server,
                key=lambda number_of_data_center: data_centers_of_active_server[
                                                      number_of_data_center
                                                  ] * data_center_resets[number_of_data_center])
            print(max_data_center)

        if 'GETMIN' in line:
            min_data_center = min(
                data_centers_of_active_server,
                key=lambda number_of_data_center: data_centers_of_active_server[
                                                      number_of_data_center
                                                  ] * data_center_resets[number_of_data_center])
            print(min_data_center)


data_collection_about_data_center(count_data_centers, count_of_servers, event_count)