def day1task2():
    with open('inputs/day1.txt') as f:
        data = f.readlines()
    data = [int(x.strip()) for x in data]

    # Test data
    # data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    total = 0

    windows = []

    # Loop over the data
    for i in range(len(data)):
        # Make sure that there are more than 3 elements ahead of data[i]
        if i + 3 <= len(data):
            # Get 3 elements in an array and add them to the windows
            windows.append(data[i:i + 3])
        else:
            break

    sums = []

    # Loop over the windows
    for window in windows:
        sums.append(sum(window))

    # Loop over the sums
    for i in range(len(sums)):
        # If this is the first element, skip
        if i == 0:
            continue

        # If the current sum is more than the previous, add 1 to total
        if sums[i] > sums[i - 1]:
            total += 1

    print(total)


if __name__ == '__main__':
    day1task2()
