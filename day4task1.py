def day4task1():
    drawn, boards = get_data()

    drawn_to_be_checked = []
    for draw in drawn:
        drawn_to_be_checked.append(int(draw))
        for board in boards:
            if check_win(board, drawn_to_be_checked):
                print(f"Answer: {drawn_to_be_checked[-1] * sum(get_left_over_numbers(board, drawn_to_be_checked))}")
                return


def get_data() -> (list[str], list[list[int]]):
    with open('inputs/day4.txt', 'r') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    drawn = data[0].split(',')
    data = data[2:]
    for i in range(len(data)):
        data[i] = extract_numbers_from_string(data[i])
    # Remove empty arrays from data
    data = [x for x in data if x]
    # Generate boards by making a 2D array with 5 columns of data
    boards = []
    for i in range(0, len(data), 5):
        boards.append(data[i:i + 5])
    return drawn, boards


def extract_numbers_from_string(string: str) -> list:
    return [int(s) for s in string.split() if s.isdigit()]


def get_left_over_numbers(board: list[int], drawn: list[int]) -> list[int]:
    left_over = []
    for row in board:
        for num in row:
            if num not in drawn:
                left_over.append(num)
    return left_over


def check_win(board: list[int], drawn: list[int]) -> bool:
    for row in board:
        row_got = 0
        for num in row:
            if num in drawn:
                row_got += 1
        if row_got == 5:
            return True

    for i in range(5):
        col = []
        for row in board:
            col.append(row[i])
        col_got = 0
        for num in col:
            if num in drawn:
                col_got += 1
        if col_got == 5:
            return True

    return False


if __name__ == "__main__":
    day4task1()
