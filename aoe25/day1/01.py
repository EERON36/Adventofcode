def main():
    position = 50
    global counter
    counter = 0
    # laps = 0

    with open("dial.txt", "r") as code:
        for line in code:
            line = line.strip()

            direction = line[0]
            code = int(line[1:])

            # coiunt laps
            if code >= 100:
                counter = counter + code // 100
                # counter = counter + laps
                print(f" LLAPS {laps} AND CODE {code}")

            # figure out enw position
            remainder = code % 100

            if direction == "R":
                new_position = position + remainder

                if new_position > 100:
                    counter = counter + 1

                position = new_position % 100

            else:  # LX -> R(100-X)

                if position is not 0:

                    if remainder > position:
                        counter = counter + 1

                new_position = position + (100 - remainder)
                position = new_position % 100

            if position == 0:
                counter = counter + 1

            # counter = counter + laps

            print(f"Code {line}")
            print(f"Position {position}")
            print(f"Laps {laps} Counter {counter}")


# Run the program
if __name__ == "__main__":
    main()
