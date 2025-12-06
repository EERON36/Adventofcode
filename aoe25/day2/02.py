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
            print(f"First_part = {first_part} Secon part = {second_part}")

            # Loops 3?
