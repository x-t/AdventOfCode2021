from part1 import get_data, check_win, get_left_over_numbers


def day4part2(file_input: str) -> int:
    drawn, boards = get_data(file_input)
    boards_won = 0
    boards_to_win = len(boards)
    boards_won_idx = []

    drawn_to_be_checked = []
    for draw in drawn:
        drawn_to_be_checked.append(int(draw))
        for i in range(len(boards)):
            if i in boards_won_idx:
                continue
            if check_win(boards[i], drawn_to_be_checked):
                boards_won += 1
                boards_won_idx.append(i)
            if boards_won == boards_to_win:
                last_board = boards[boards_won_idx[-1]]
                last_check = drawn_to_be_checked[-1]
                return last_check * sum(get_left_over_numbers(last_board, drawn_to_be_checked))


if __name__ == "__main__":
    print(day4part2('input.txt'))
