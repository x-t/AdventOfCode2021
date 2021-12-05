import copy

from day3task1 import get_data


def day3task2():
    _bytes = get_data()

    _bytes_copy = copy.deepcopy(_bytes)
    oxygen_generator_rating = ['0']
    co2_scrubber_rating = ['0']

    for i in range(len(_bytes)):
        indexes_worth_using = filter_out(_bytes, i, count(_bytes, i))
        if len(indexes_worth_using) == 1:
            oxygen_generator_rating = list(construct(_bytes, indexes_worth_using[0]))
            break

    _bytes = _bytes_copy

    for i in range(len(_bytes)):
        indexes_worth_using = filter_out(_bytes, i, count(_bytes, i, True))
        if len(indexes_worth_using) == 1:
            co2_scrubber_rating = list(construct(_bytes, indexes_worth_using[0]))
            break

    # Convert list of 1s and 0s of binary number to decimal
    oxygen_generator_rating_dec = int(''.join(oxygen_generator_rating), 2)
    co2_scrubber_rating_dec = int(''.join(co2_scrubber_rating), 2)
    print(f"Oxygen: {oxygen_generator_rating_dec}\nCO2: {co2_scrubber_rating_dec}")
    print(f"Answer: {oxygen_generator_rating_dec * co2_scrubber_rating_dec}")


def count(_bytes, on_index, co2_mode=False):
    zeroes = _bytes[on_index].count('0')
    ones = _bytes[on_index].count('1')
    if not co2_mode:
        if zeroes > ones:
            return '0'
        else:
            return '1'
    else:
        if zeroes > ones:
            return '1'
        else:
            return '0'


def filter_out(_bytes, on_index, keep):
    indexes_to_keep = []
    for i in range(len(_bytes[on_index])):
        if _bytes[on_index][i] == keep:
            indexes_to_keep.append(i)
    # Remove indexes from _bytes
    for i in range(len(_bytes)):
        for j in range(len(_bytes[i])):
            if j not in indexes_to_keep:
                _bytes[i][j] = ''
    return indexes_to_keep


def construct(_bytes, on_index):
    # Construct binary number from _bytes
    binary = ''
    for i in range(len(_bytes)):
        binary += _bytes[i][on_index]
    return binary


if __name__ == "__main__":
    day3task2()
