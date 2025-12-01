def rdial(turndial, code):
    total = turndial + code
    while total > 99:
        total = total - 100
    return total


def ldial(turndial, code):
    total = turndial - code
    while total < 0:
        total = total + 100
    return total


def main():
    position = 50
    counter = 0

    with open("dial.txt", "r") as code:
        for line in code:
            print(line)
            print(position)
            if line[0] == "R":
                position = rdial(position, int(line[1:]))

            else:
                position = ldial(position, int(line[1:]))

            if position == 0:
                counter += 1

        print(counter)


# Run the program
if __name__ == "__main__":
    main()
