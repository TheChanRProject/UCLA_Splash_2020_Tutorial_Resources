from os import getcwd

file_path = getcwd() + "/ideas/my_file.txt"

my_list = []

with open(f"{file_path}", "r") as my_file:
    for line in my_file.readlines():
        line = line.replace("\n", "")
        my_list.append(line)

my_list

my_num = "".join(my_list)

my_num = int(my_num)

my_num % 2 == 0
