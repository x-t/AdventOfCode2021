from day5task1 import get_matrix_size, get_data, leave_only_straight_lines, count_overlaps


def day5task2():
    straights = leave_only_straight_lines(get_data(True))
    diagonals = leave_diagonals(get_data(True))
    matrix_size = get_matrix_size(straights)
    matrix = [[0 for _ in range(matrix_size[0])] for _ in range(matrix_size[1])]
    matrix = proper_draw_straights(straights, matrix)
    # Flip matrix back
    matrix = [[matrix[y][x] for y in range(matrix_size[1])] for x in range(matrix_size[0])]
    matrix = draw_diagonals(diagonals, matrix)

    # for line in matrix:
    #     print(line)
    print(f"Answer: {count_overlaps(matrix)}")
    return


# Considering, this still draws them flipped, I don't know, but it doesn't touch the data.
def proper_draw_straights(data: list[list[list[int]]], matrix: list[list[int]]) -> list[list[int]]:
    for line in data:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]
        # Which direction?
        if x1 == x2:
            # Vertical
            if y1 < y2:
                # Down
                for y in range(y1, y2 + 1):
                    matrix[x1][y] += 1
            else:
                # Up
                for y in range(y1, y2 - 1, -1):
                    matrix[x1][y] += 1
        else:
            # Horizontal
            if x1 < x2:
                # Right
                for x in range(x1, x2 + 1):
                    matrix[x][y1] += 1
            else:
                # Left
                for x in range(x1, x2 - 1, -1):
                    matrix[x][y1] += 1
        # for _line in matrix:
        #     print(_line)
    return matrix


def leave_diagonals(data: list[list[list[int]]]) -> list[list[list[int]]]:
    # Remove all elements that are not straight lines
    data = [x for x in data if x[0][0] != x[1][0] and x[0][1] != x[1][1]]
    return data


def draw_diagonals(data: list[list[list[int]]], matrix: list[list[int]]) -> list[list[int]]:
    for line in data:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]

        # Calculate direction
        if x1 > x2 and y1 < y2:
            # Up-right
            for x in reversed(range(x2, x1 + 1)):
                matrix[y1][x] += 1
                y1 += 1
        elif x1 > x2 and y1 > y2:
            # Up-left
            for x in reversed(range(x2, x1 + 1)):
                matrix[y1][x] += 1
                y1 -= 1
        elif x1 < x2 and y1 < y2:
            # Down-right
            for x in range(x1, x2 + 1):
                matrix[y1][x] += 1
                y1 += 1
        elif x1 < x2 and y1 > y2:
            # Down-left
            for x in range(x1, x2 + 1):
                matrix[y1][x] += 1
                y1 -= 1

    return matrix


if __name__ == "__main__":
    day5task2()
