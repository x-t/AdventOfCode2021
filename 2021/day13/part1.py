def day13part1(filename: str) -> int:
    coords, folds, canvas = setup_data(filename)
    fold_by, fold_at = folds[0]
    canvas = make_fold(canvas, fold_by, fold_at)
    return count_hashes(canvas)


def setup_data(filename: str) -> (list, list, list):
    coords, folds = split_input(get_input(filename))
    coords, folds = fix_data(coords, folds)
    max_x = max([x[0] for x in coords])
    max_y = max([x[1] for x in coords])
    canvas = make_canvas(max_x, max_y, coords)
    return coords, folds, canvas


# I literally do not know why, maybe I'm too tired, too stupid,
# or too drunk, but for the damn life of me, I cannot understand
# why this doesn't work with part 2. It follows the procedure as
# described, and still gets really stupid off-by-one errors.
def make_fold(canvas: list, fold_by: str, fold_at: int) -> list:
    canvas1 = []
    canvas2 = []
    if fold_by == 'x':
        canvas1 = [x[:fold_at] for x in canvas]
        canvas2 = [x[fold_at + 1:] for x in canvas]
        # Reverse each element of each canvas2 row
        canvas2 = [x[::-1] for x in canvas2]
    elif fold_by == 'y':
        canvas1 = canvas[:fold_at]
        canvas2 = canvas[fold_at + 1:]
        canvas2 = canvas2[::-1]
    # Join the two parts
    for i in range(len(canvas2)):
        for j in range(len(canvas2[i])):
            if canvas2[i][j] == '#':
                canvas1[i][j] = '#'
    return canvas1


def make_canvas(max_x: int, max_y: int, dots: list) -> list:
    canvas = []
    for _ in range(max_y + 1):
        canvas.append([' '] * (max_x + 1))
    for dot in dots:
        canvas[dot[1]][dot[0]] = '#'
    return canvas


def count_hashes(canvas: list) -> int:
    count = 0
    for row in canvas:
        for col in row:
            if col == '#':
                count += 1
    return count


def get_input(filename: str) -> list:
    with open(filename) as f:
        return [line.strip('\n') for line in f]


def split_input(_input: list) -> (list, list):
    coords = []
    folds = []
    add_to = coords
    for i in _input:
        if i == '':
            add_to = folds
        else:
            add_to.append(i)
    return coords, folds


def fix_data(coords: list, folds: list) -> (list, list):
    coords = [x.split(',') for x in coords]
    coords = [[int(x) for x in y] for y in coords]
    folds = [x.split(' ') for x in folds]
    folds = [x[2] for x in folds]
    folds = [x.split('=') for x in folds]
    folds = [[x[0], int(x[1])] for x in folds]
    return coords, folds


if __name__ == "__main__":
    print(day13part1("input.txt"))
