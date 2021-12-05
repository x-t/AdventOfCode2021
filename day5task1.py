"""
This manipulates the data and then prints the
matrix wrong-way-round, but it will give you
the right answer anyway.
"""


def day5task1():
    data = leave_only_straight_lines(get_data())
    matrix_size = get_matrix_size(data)
    matrix = [[0 for _ in range(matrix_size[0])] for _ in range(matrix_size[1])]
    matrix = draw_matrix(data, matrix)
    print(f"Answer: {count_overlaps(matrix)}")
    return


def draw_matrix(data: list[list[list[int]]], matrix: list[list[int]]) -> list[list[int]]:
    for line in data:
        for x in range(line[0][0], line[1][0] + 1):
            for y in range(line[0][1], line[1][1] + 1):
                matrix[x][y] += 1

    return matrix


def get_data(dont_touch=False) -> list[list[list[int]]]:
    with open('inputs/day5.txt', 'r') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    # Split each element by spaces
    data = [x.split(' ') for x in data]
    # Remove second element of each list
    data = [[x[0], x[2]] for x in data]
    # Split each element by ','
    data = [[x[0].split(','), x[1].split(',')] for x in data]
    # Convert each element to int
    data = [[[int(x[0]), int(x[1])] for x in y] for y in data]
    if not dont_touch:
        for d in data:
            # If x1 > x2, swap x1 and x2
            if d[0][0] > d[1][0]:
                d[0], d[1] = d[1], d[0]
            # If y1 > y2, swap y1 and y2
            if d[0][1] > d[1][1]:
                d[0], d[1] = d[1], d[0]
    return data


def leave_only_straight_lines(data: list[list[list[int]]]) -> list[list[list[int]]]:
    # Remove all elements that are not straight lines
    data = [x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    return data


def get_matrix_size(data: list[list[list[int]]]) -> list[int]:
    x_max = 0
    y_max = 0
    for line in data:
        x_max = max(x_max, line[0][0], line[1][0])
        y_max = max(y_max, line[0][1], line[1][1])
    return [x_max + 1, y_max + 1]


def count_overlaps(matrix: list[list[int]]) -> int:
    count = 0
    for line in matrix:
        for x in line:
            if x > 1:
                count += 1
    return count


if __name__ == "__main__":
    day5task1()
