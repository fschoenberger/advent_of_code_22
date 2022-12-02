from functools import reduce

def main():
    with open("./Puzzle 01.txt") as f:        
        input = f.read()

        current_max = 0
        elf_index = 0

        elves = input.split("\n\n")
        print(elves)

        elves_calories = []

        for i, elf_inventory_string in enumerate(elves):
            elf_inventory = elf_inventory_string.split("\n")
            aggregate = reduce(lambda x, y: int(x) + int(y), elf_inventory, 0)
            print(f"Elf {i} has total calories of {aggregate}")

            elves_calories.append(aggregate)

        elves_calories = sorted(elves_calories)
        top_three_calories = elves_calories[-1] + elves_calories[-2] + elves_calories[-3]

        print(f"Result: {top_three_calories}")

if __name__ == "__main__":
    main()