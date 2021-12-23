
def read_file(fname: str):
    file = open(fname, 'r')
    file_str = [line.split(',') for line in file][0]
    file_int = [int(char) for char in file_str]
    return file_int


def build_fish_dict(states_list: list) -> dict:
        fish_dict = {}
        for count, state in enumerate(states_list):
            fish_dict[count] = state
        return fish_dict


def loop_fish(fish_dict: dict, days: int) -> dict:

    while days > 0:
        print(days)
        for key in fish_dict.copy():
            fish_dict[key] -= 1
            # check for reset
            if fish_dict[key] < 0:
                fish_dict[key] = 6
                fish_dict[len(fish_dict)] = 8

        days -= 1
    return fish_dict


def main():
    states = read_file('AoC_6.txt')
    days = 80

    fish_dict = build_fish_dict(states)
    model = loop_fish(fish_dict, days)
    print(len(model))


if __name__ == '__main__':
    main()


# for part 2 try doing this another way, having the states as the disctionary keys and the fish as the values in a list?