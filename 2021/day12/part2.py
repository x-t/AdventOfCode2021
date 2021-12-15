from part1 import get_input, add_missing_info, map_input


def day12part2(filename: str) -> int:
    _input = get_input(filename)
    _map = add_missing_info(map_input(_input))
    paths = find_all_paths(_map, 'start', 'end')
    return len(paths)


# Code duplication is my middle name.
# Also, it's genuinely slow for the real input, not so much for the tests.
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node != 'start':
            if not node.islower() or node == 'end':
                paths += find_all_paths(graph, node, end, path)
            elif count_occurrences(path, node) < 2:
                lowercase = get_lowercase(path)
                if len(lowercase) > 0:
                    counts = [count_occurrences(path, i) for i in lowercase]
                    if max(counts) == 2 and node in path:
                        continue
                paths += find_all_paths(graph, node, end, path)
    return paths


# Get amount of times value is in list
def count_occurrences(_list, value):
    return len([i for i in _list if i == value])


def get_lowercase(_list):
    return list(set([i for i in _list if i.islower() and i != 'start']))


if __name__ == '__main__':
    print(day12part2('input.txt'))
