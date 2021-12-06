def day1part1(file_input: str) -> int:
    with open(file_input) as f:
        data = f.readlines()
    data = [int(x.strip()) for x in data]

    total = 0

    # Loop through data
    for i in range(len(data)):
        # If on first element, skip
        if i == 0:
            continue

        # If current element is more than previous element, add to total
        if data[i] > data[i - 1]:
            total += 1

    return total


if __name__ == '__main__':
    print(day1part1('input.txt'))
