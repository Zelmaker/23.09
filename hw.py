def choose_function(func_to_do, value, file):
    linux_dict = {"filter": linux_filter,
                  "map": linux_map,
                  "unique": linux_unique,
                  "sort": linux_sort,
                  "limit": linux_limit,
                  }
    if func_to_do not in linux_dict:
        exit("Не правильный ввод")
    else:
        file_filtered = linux_dict.get(func_to_do)(value, file)
        print(f"Выполняю {func_to_do} - со значением {value}")
    return file_filtered


def linux_filter(value, file):
    filtered_file = []
    for i in file:
        if value in i:
            filtered_file.append(i)
    return filtered_file


def linux_map(value, file):
    filtered_file = []
    for string in file:
        newstring = string.strip().split(" ")
        filtered_file.append(newstring[int(value)])
    return filtered_file


def linux_unique(value, file):
    return list(set(file))


def linux_sort(value, file):
    reverse_par = False
    if value == "asc":
        reverse_par = False
    elif value == "desc":
        reverse_par = True
    return sorted(file, key=None, reverse=reverse_par)


def linux_limit(value, file):
    count = 0
    filtered_file = []
    for i in file:
        if count <= int(value) - 1:
            count += 1
            filtered_file.append(i)
        else:
            break
    return filtered_file


def reading_file():
    with open("apache_logs.txt", 'r', encoding="utf-8") as f:
        contents = f.readlines()
    return contents


def split_input_to_commands(user_input):
    command_dict = {}
    if " " not in user_input.strip():
        exit("Не правильный ввод")

    else:
        user_input_commands = user_input.split("|")
        for i in user_input_commands:
            key, value = i.strip().split(" ")
            command_dict[key] = value
    return command_dict







def main():
    print("Доступные linux команды : filter, map, unique, sort, limit")
    print("Команды записываются через разделитель “|”.")
    print("Укажите 2 команды")
    user_input = input()
    user_commands_dict = split_input_to_commands(user_input)
    content = reading_file()
    for k, v in user_commands_dict.items():
        content = choose_function(k, v, content)
    for line in content:
        print(line)


if __name__ == '__main__':
    main()
