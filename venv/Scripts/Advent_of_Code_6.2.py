

def read_file(fname: str) -> list:
    file = open(fname, 'r')
    file_str = [line.split(',') for line in file][0]
    file_int = [int(char) for char in file_str]
    return file_int


def build_fish_dict(states_list: list) -> dict:
    fish_dict = {0: 0,
                 1: 0,
                 2: 0,
                 3: 0,
                 4: 0,
                 5: 0,
                 6: 0,
                 7: 0,
                 8: 0,}

    for state in states_list:
        if state not in fish_dict:
            fish_dict[state] = 1
        else:
            fish_dict[state] += 1
    return fish_dict


def loop_fish(fish_dict: dict, days: int) -> dict:
    store_6 = 0
    store_8 = 0
    while days > 0:
        copied = fish_dict.copy()
        for key in copied:
            # print('key ' + str(key))
            # print('value ' + str(fish_dict[key]))
            if (key == 0) and (fish_dict[key] > 0):
                store_6 = fish_dict[key]
                store_8 = fish_dict[key]
            elif (key == 0) and (fish_dict[key] == 0):
                pass
            else:
                # print('else')
                fish_dict[key - 1] = fish_dict[key]


        fish_dict[6] = store_6
        fish_dict[8] = store_8

        days -= 1
        print(fish_dict)
        print(sum(fish_dict.values()))
    return fish_dict

def main():
    states = read_file('AoC_6.txt')
    days = 18
    fish_dict = build_fish_dict(states)
    print('start')
    print(fish_dict)
    print('model')
    model = loop_fish(fish_dict, days)
    print(sum(model.values()))

if __name__ == '__main__':
    main()

