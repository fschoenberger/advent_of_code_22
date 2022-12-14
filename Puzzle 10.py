def main():
    instructions = []

    with open("./Puzzle 10.txt") as f:
        for line in f.readlines():
            if line.startswith("noop"):
                instructions.append({'type': 'noop', 'cycles': 1})
            if line.startswith("addx"):
                # We normalize this
                instructions.append({'type': 'noop', 'cycles': 1})
                num = int(line[5:-1])
                instructions.append({'type': 'addx', 'arg': num, 'cycles': 1})

    x_register = [1]
    cycles = 0

    for instruction in instructions:
        cycles += instruction['cycles']
        if instruction['type'] == 'noop':
            # print("noop")
            x_register.append(x_register[-1])
        elif instruction['type'] == 'addx':
            # print(f"addx {instruction['arg']}")
            # x_register.append(x_register[-1])
            x_register.append(x_register[-1] + instruction['arg'])

    sum = 20 * x_register[19] + 60 * x_register[59] + 100 * x_register[99] + 140 * x_register[139] + 180 * x_register[179] + 220 * x_register[219]
    
    print(
        f"The signal strength measurements were t=20,x={x_register[19]}, t=60,v={x_register[59]}, t=100,x={x_register[99]}, "
        + f"t=140,x={x_register[139]}, t=180,x={x_register[179]} and t=220,x={x_register[219]}. The sum was {sum}.")

    screen_list = ["." for i in range(240)]
    sprite_position = 1
    
    for current_cycle, instruction in enumerate(instructions):
        implied_position = current_cycle % 40
        if sprite_position - 1 <= implied_position and sprite_position + 1 >= implied_position:
            screen_list[current_cycle] = "#"
        
        if instruction['type'] == 'addx':
            # print(f"addx {instruction['arg']}")
            # x_register.append(x_register[-1])
            sprite_position += instruction['arg']

    screen = "".join(screen_list)
    print(f"{screen[0:39]}\n{screen[40:79]}\n{screen[80:119]}\n{screen[120:159]}\n{screen[160:199]}\n{screen[200:239]}")

    


if __name__ == "__main__":
    main()
