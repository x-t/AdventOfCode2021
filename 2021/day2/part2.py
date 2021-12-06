def day2part2(file_input: str) -> int:
    with open(file_input, 'r') as f:
        data = f.readlines()

    # Strip newline characters
    data = [x.strip() for x in data]

    # Split each input by space
    data = [x.split(' ') for x in data]

    final_horizontal_position = 0
    final_depth = 0
    aim = 0

    for i in range(len(data)):
        if data[i][0] == 'up':
            aim -= int(data[i][1])
        elif data[i][0] == 'down':
            aim += int(data[i][1])
        elif data[i][0] == 'forward':
            final_horizontal_position += int(data[i][1])
            final_depth += aim * int(data[i][1])

    return final_horizontal_position * final_depth


if __name__ == '__main__':
    print(day2part2('input.txt'))
