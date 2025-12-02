def main():
    position = 50
    global counter
    counter = 0

    with open("dial.txt", "r") as code:
        for line in code:
            line = line.strip()

        if int(line[1:] >= 100):
            # 100 = 1 varv
            # räkna hur nånga
            # mod 100 för rest värdet

            # left turn
            # samam sak som right,
            """Pos 25 -> L50
            25 -> 75
            100-25 = 50 -> R50
            25+50 = 75"""


# Run the program
if __name__ == "__main__":
    main()
