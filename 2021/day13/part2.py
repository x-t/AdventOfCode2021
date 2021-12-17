# I genuinely HATED this problem.
# The whole "let's give a test case too small to fail" thing is a huge pain.
# I seriously don't consider this one solved, as I looked at the solutions
# afterwards. I do not regret it.

from part1 import setup_data


def day13part2(filename: str) -> int:
    coords, folds, _ = setup_data(filename)
    points = set()
    for coord in coords:
        x, y = coord
        points.add((x, y))
    for fold_by, fold_at in folds:
        for coord in list(points):
            points.remove(coord)
            x, y = coord
            # Yeah, sure, whatever. Do whatever you want.
            # Why not << 1 instead of times?
            if fold_by == "x" and x > fold_at:
                x = 2 * fold_at - x
            elif fold_by == "y" and y > fold_at:
                y = 2 * fold_at - y
            points.add((x, y))

    # Splits the X'es and Y'es?
    # I guess??
    whatever1, whatever2 = zip(*points)

    for y in range(max(whatever2) + 1):
        for x in range(max(whatever1) + 1):
            if (x, y) in points:
                print(" #", end="")
            else:
                print("  ", end="")
        print()

    return 0


if __name__ == "__main__":
    print(day13part2("input.txt"))
