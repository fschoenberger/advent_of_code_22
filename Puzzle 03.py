def to_priority(item: str):
    ascii_dec = ord(item)
    if ascii_dec <= 90 and ascii_dec >= 65:
        return ascii_dec - 38
    else:
        return ascii_dec - 96

def main():
    with open("./Puzzle 03.txt") as f:
        compartments = [(set(f[:len(f) // 2]), set(f[len(f) // 2:])) for f in f.readlines()]
        # print(compartments)
        matching = map(lambda x: list(x[0].intersection(x[1]))[0], compartments)
        # print(matching)

        priorities = map(to_priority, matching)
        # print(priorities)

        print(f"The sum of the priorities is {sum(priorities)}")

def main_2():
    with open("./Puzzle 03.txt") as f:
        lines = f.readlines()

        groups = [(set(lines[3 * i][:-1]), set(lines[3 * i + 1][:-1]), set(lines[3 * i + 2][:-1])) for i in range(len(lines) // 3)]
        # print(groups)
        badges = [list((g[0].intersection(g[1])).intersection(g[2]))[0] for g in groups]
        # print(badges)
        priorities = map(to_priority, badges)
        print(f"The total sum of priorities for the badges is {sum(priorities)}")

if __name__ == "__main__":
    main()