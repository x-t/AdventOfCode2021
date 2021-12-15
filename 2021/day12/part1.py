import copy


def day12part1(filename: str) -> int:
    _input = get_input(filename)
    _map = add_missing_info(map_input(_input))
    paths = find_all_paths(_map, 'start', 'end')
    return len(paths)


# I stole this one shamelessly too.
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if not node.islower():
            paths += find_all_paths(graph, node, end, path)
        elif node not in path:
            paths += find_all_paths(graph, node, end, path)
    return paths


def add_missing_info(_map: dict) -> dict:
    _map_copy = copy.deepcopy(_map)
    for key, value in _map.items():
        for i in value:
            if i not in _map_copy:
                _map_copy[i] = []
            _map_copy[i].append(key)
    return _map_copy


def get_input(filename: str) -> list:
    _input = []
    with open(filename) as f:
        _input = f.read().splitlines()
    _input = [x.split('-') for x in _input]
    return _input


def map_input(_input: list) -> dict:
    _map = {}
    for i in _input:
        if i[0] not in _map:
            _map[i[0]] = []
        _map[i[0]].append(i[1])
    return _map


if __name__ == '__main__':
    print(day12part1('input.txt'))
