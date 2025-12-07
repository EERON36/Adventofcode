def find_invalid(number):
    # find_invalid(number, index, size)
    # if index < 0 or index > len(number) - 1:
    #     return False

    # if index + size * 2 > len(number) - 1:
    #     return False

    # first_value = number[index : index + size - 1]
    # second_value = number[index + size : index + size * 2 - 1]

    # if first_value == second_value:
    #     return True

    # return find_invalid(number, index + 1, size) or find_invalid(
    #     number, index, size + 1
    # )

    # test for seq of 4
    # then 3, 2 ,1
    lenght = len(number)
    floor_lenght = lenght // 2

    for num in range(1, floor_lenght + 1):
        # check if / 2 is even
        if lenght % num is not 0:
            continue
        else:
            seq = number[0:num]
            checker = num // floor_lenght

            if seq * checker == number:
                return True
            # seq_two = number[num:]

    return False


def main():
    invalid_id = 0
    with open("test.txt", "r") as file:
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

                    if find_invalid(s_str):
                        print(s_str)

                    # lenght_pairs = int(lenght_s / 2)

                    # if lenght_s % 2 == 0:
                    #     # index till split
                    #     first = s_str[0:lenght_pairs]
                    #     # print(first)
                    #     # index split + resten
                    #     second = s_str[lenght_pairs:]
                    #     # print(second)
                    #     if first == second:
                    #         invalid_id = invalid_id + s
                    #     else:
                    #         continue


if __name__ == "__main__":
    main()
