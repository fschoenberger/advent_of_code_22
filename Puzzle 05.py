import re

def parse_stack_lines(section: str):
    num_stacks = int(re.match(".* (\d+) *$", section.splitlines()[-1]).groups()[0])
    stacks_regex = re.compile("^" + (num_stacks - 1) * "(\[[A-Z]+\]| {3}) " + "(\[[A-Z]+\]| {3})")

    stacks_lines = section.splitlines()[:-1]
    stacks_lines.reverse()
    stacks_table = map(lambda l: stacks_regex.match(l).groups(), stacks_lines)
    # print(list(stacks_table))

    stacks = [[] for i in range(num_stacks)]

    for stacks_line in stacks_table:
        for i, stack_group in enumerate(stacks_line):
            if stack_group.strip() != "":
                stacks[i].append(stack_group[1:-1])

    # print(stacks)
    return stacks


def main():
    with open("Puzzle 05.txt") as f:
        file_parts = f.read().split("\n\n")

        stacks = parse_stack_lines(file_parts[0])

        for instruction in file_parts[1].splitlines():
            regex = re.compile("^move (\d*) from (\d+) to (\d+)$")
            matches = regex.match(instruction).groups()

            amount = int(matches[0])
            from_stack = int(matches[1]) - 1
            to_stack = int(matches[2]) - 1

            # First part 
            #for i in range(amount):
            #    stacks[to_stack].append(stacks[from_stack].pop())

            print(stacks)

            boxes = stacks[from_stack][(-amount):]
            del stacks[from_stack][(-amount):]
            stacks[to_stack].extend(boxes)

        print(stacks)
        print(list(map(lambda s: s[-1], stacks)))
       

if __name__ == "__main__":
    main()