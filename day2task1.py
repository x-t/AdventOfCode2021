def day2task1():
    with open('inputs/day2.txt', 'r') as f:
        data = f.readlines()

    # Strip newline characters
    data = [x.strip() for x in data]

    # Split each input by space
    data = [x.split(' ') for x in data]

    final_horizontal_position = 0
    final_depth = 0

    for i in range(len(data)):
        if data[i][0] == 'up':
            final_depth -= int(data[i][1])
        elif data[i][0] == 'down':
            final_depth += int(data[i][1])
        elif data[i][0] == 'forward':
            final_horizontal_position += int(data[i][1])

    print(final_horizontal_position * final_depth)


if __name__ == '__main__':
    day2task1()
