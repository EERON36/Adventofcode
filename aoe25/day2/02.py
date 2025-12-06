with open("test.txt", "r") as file:
    for line in file:
        id_list = line.strip().split(",")
        print(id_list)

        for group in id_list:
            print("Group")
            print(group)
