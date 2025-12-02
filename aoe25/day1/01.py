def rdial(turndial, code):
    total = turndial + code
    print(f"Righ dial current position {total}")
    global counter
    if total == 0:
        counter = counter + 1
        print("CAUGHT YOU BITCH")
    while total > 99:
        if code == 0:
            break
        else:
            if turndial is not 0:
                counter = counter + 1
            total = total - 100
        # print("global +1")
        # print(counter)
    print(f"Final counter Right {counter}")
    print(f"Final Position R {total}")
    return total


def ldial(turndial, code):
    total = turndial - code
    print(f"Left dial current position {total}")
    global counter
    if total == 0:
        counter = counter + 1
        print("CAUGHT YOU BITCH")
    while total <= -1:
        if code == 0:
            break
        else:
            if turndial is not 0:
                counter = counter + 1
            total = total + 100
        # print("global +1")
        # print(counter)
    print(f"Final counter Left {counter}")
    print(f"Final Position L {total}")
    return total


def main():
    position = 50
    global counter
    counter = 0

    with open("dial.txt", "r") as code:
        for line in code:
            line = line.strip()
            print(line)
            # print(position)
            if line[0] == "R":
                position = rdial(position, int(line[1:]))

            else:
                position = ldial(position, int(line[1:]))

            # if position == 0:
            #     counter += 1
            # print(f"Added +1 in last if counter {counter} and position was {position}")

        print(f"Final position {position}")
        print(f"Final counter {counter}")


# Run the program
if __name__ == "__main__":
    main()
