

### Future Scope
# build number class
    # should be able to display number (is this __repr__ or __String__
    # should count the number of segments

# need a dictionary of segments counts and the number that use them - so 3 would be 7, 4 would be 4

from Digit import Segment

def read_file(fname: str) -> list:
    with open(fname, 'r') as file:
        file = file.read()
        split_file = file.split('\n')
        very_split = [element.strip().split(' | ') for element in split_file]
        obj_list = []
        x = 1
        for element in very_split:
            for seg in element[0].split(' '):
                seg_obj = Segment(seg, 'signal', x)
                obj_list.append(seg_obj)

            for seg in element[1].split(' '):
                seg_obj = Segment(seg, 'output', x)
                obj_list.append(seg_obj)
            x += 1

        return obj_list


def check_segments(values: list) -> int:
    # first build a list of all the output values
    all_out = []
    for element in values:
        if element.type == 'output':
            all_out.append((element.signal, element.count()))

    # check all output values for result
    counter = 0
    for val in all_out:
        if val[1] == 2:
            counter += 1
        elif val[1] == 3:
            counter += 1
        elif val[1] == 4:
            counter += 1
        elif val[1] == 7:
            counter += 1

    return counter


def main():
    values = read_file('AoC_8.txt')


    # segments = {1: (None, ),
    #             2: (1, ),
    #             3: (7, ),
    #             4: (4, ),
    #             5: (2, 3, 5),
    #             6: (6, 9),
    #             7: (8, )}

    result = check_segments(values)
    print(result)

if __name__ == '__main__':
    main()