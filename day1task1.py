def day1task1():
    with open('inputs/day1.txt') as f:
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

    print(total)


if __name__ == '__main__':
    day1task1()
