def day3part1(file_input: str) -> int:
    _bytes = get_data(file_input)

    gamma_rate = []
    epsilon_rate = []

    for i in range(len(_bytes)):
        # Count zeroes
        zeroes = _bytes[i].count('0')
        # Count ones
        ones = len(_bytes[0]) - zeroes

        if zeroes > ones:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')

    # Convert list of 1s and 0s of binary number to decimal
    gamma_dec = int(''.join(gamma_rate), 2)
    epsilon_dec = int(''.join(epsilon_rate), 2)
    # print(f"Gamma: {gamma_dec}\nEpsilon: {epsilon_dec}")
    return gamma_dec * epsilon_dec


def get_data(file_input: str) -> list[list[str]]:
    with open(file_input, 'r') as f:
        data = f.readlines()

    # Trim newlines
    data = [x.strip() for x in data]
    byte_len = len(data[0])
    _bytes = []

    for i in range(byte_len):
        _bytes.append([])

    for byte in data:
        for i in range(byte_len):
            _bytes[i] += byte[i]
    return _bytes


if __name__ == "__main__":
    print(day3part1('input.txt'))
