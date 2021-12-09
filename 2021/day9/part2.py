import copy

from part1 import find_low_points, get_input


def day9part2(filename: str) -> int:
    heightmap = add_padding(get_input(filename))
    low_points = find_low_points(heightmap)
    basins = []
    for point in low_points:
        fill = flood_fill(copy.deepcopy(heightmap), point[1], point[0], 10)
        count = count_in_2d_arr(fill, 10)
        basins.append(count)
    # Last 3 sorted elements are the largest basins
    largest_basins = sorted(basins)[-3:]
    # Multiply them all together
    return largest_basins[0] * largest_basins[1] * largest_basins[2]


def add_padding(heightmap: list) -> list:
    nines = [9] * (len(heightmap[0]) + 2)
    for line in heightmap:
        line.insert(0, 9)
        line.append(9)
    return [nines] + heightmap + [nines]


# In the amazing nature of programming, this is just stolen
# off of leetcode. Note to myself: actually learn what these
# things do.
def flood_fill(image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == new_color:
        return image

    def dfs(r, c):
        if image[r][c] != 9 and image[r][c] != 10:
            image[r][c] = new_color
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


def count_in_2d_arr(arr: list[list[int]], val: int) -> int:
    count = 0
    for line in arr:
        count += line.count(val)
    return count


if __name__ == "__main__":
    print(day9part2("input.txt"))
