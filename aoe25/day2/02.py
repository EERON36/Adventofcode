invalid_id = 0

with open("input.txt", "r") as file:
    # Loop 1
    for line in file:
        id_list = line.strip().split(",")
        # print(id_list)

        # loop 2
        for group in id_list:
            # skip last symbol
            if not group:
                continue
            # print("Group")
            # print(group)
            parts = group.split("-")
            # print("parts")
            # print(parts)
            first_part = int(parts[0])
            second_part = int(parts[1])
            # print(f"First_part = {first_part} Secon part = {second_part}")

            # loop 3
            # get lenght of string
            # find highest possible seq ex. 1010 (2) 10 10  then (1)
            # add to ivnalid ids
            # 666666
            # 3
            # 012  345
            for s in range(first_part, second_part + 1):
                lenght_s = len(str(s))
                s_str = str(s)
                lenght_pairs = int(lenght_s / 2)

                if lenght_s % 2 == 0:
                    # index till split
                    first = s_str[0:lenght_pairs]
                    # print(first)
                    # index split + resten
                    second = s_str[lenght_pairs:]
                    # print(second)
                    if first == second:
                        invalid_id = invalid_id + s
                    else:
                        continue

print(invalid_id)
