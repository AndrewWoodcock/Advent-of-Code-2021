

def read_file(fname: str) -> list:
    file = open(fname, 'r')
    file_str = [line.split(',') for line in file][0]
    file_int = [int(char) for char in file_str]
    return file_int


def build_fish_dict(states_list: list) -> dict:
    fish_dict = {}
    for i in range(9):
        fish_dict[i] = 0

    for state in states_list:
        if state not in fish_dict:
            fish_dict[state] = 1
        else:
            fish_dict[state] += 1
    return fish_dict


def loop_fish(fish_dict: dict, days: int) -> dict:

    while days > 0:
        # make a copy of the base fish_dict
        copied = fish_dict.copy()
        # 0s move to 8s (new fish)
        copied[8]= fish_dict[0]
        # 0s, move to 6s (restart cycle) + those moving from 7
        copied[6] = fish_dict[0] + fish_dict[7]
        # other numbers
        copied[7] = fish_dict[8]
        copied[5] = fish_dict[6]
        copied[4] = fish_dict[5]
        copied[3] = fish_dict[4]
        copied[2] = fish_dict[3]
        copied[1] = fish_dict[2]
        copied[0] = fish_dict[1]

        # re-apply to original dict
        fish_dict = copied.copy()
        days -= 1
    return fish_dict


def main():
    states = read_file('AoC_6.txt')
    days = 256
    fish_dict = build_fish_dict(states)
    model = loop_fish(fish_dict, days)
    print(sum(model.values()))


if __name__ == '__main__':
    main()

