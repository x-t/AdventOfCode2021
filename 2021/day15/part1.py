from queue import PriorityQueue


def day15part1(filename: str) -> int:
    grid = get_input(filename)
    go_from = (0, 0)
    go_to = (len(grid) - 1, len(grid[0]) - 1)

    cost_so_far = find_lowest_cost_path(go_from, go_to, grid)
    return cost_so_far[go_to]


def find_lowest_cost_path(go_from, go_to, grid):
    # Following code is adapted from
    # https://www.redblobgames.com/pathfinding/a-star/introduction.html
    # Thank you mate, owe you one 🙏
    frontier = PriorityQueue()
    frontier.put(go_from, False)
    came_from = dict()
    cost_so_far = dict()
    came_from[go_from] = None
    cost_so_far[go_from] = 0
    while not frontier.empty():
        current = frontier.get()

        if current == go_to:
            break

        for next in get_neighbours(current[0], current[1], grid):
            new_cost = cost_so_far[current] + grid[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    return cost_so_far


def get_neighbours(x: int, y: int, grid: list) -> list:
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < len(grid) - 1:
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < len(grid[0]) - 1:
        neighbours.append((x, y + 1))
    return neighbours


def get_input(filename: str) -> list:
    with open(filename, 'r') as f:
        return [[int(x) for x in list(line.strip())] for line in f.readlines()]


if __name__ == '__main__':
    print(day15part1('input.txt'))
