
import numpy as np


class Position:

    def __init__(self, pos, up, down, left, right):
        self.pos = pos
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __iter__(self):
        return self

    def __next__(self):
        return self

    def is_low(self):
        heights = [self.up, self.down, self.left, self.right]
        return all(i > self.pos for i in heights if i != None)


def read_file(fname: str) -> tuple:
    with open(fname, 'r') as file:
        file = file.read()
        num_list = [int(char) for char in file if char != '\n']
        return num_list


def to_array(num_list: list, cols: int, rows: int,) -> np.ndarray:
    num_array = np.array(num_list).reshape(cols, rows)
    return num_array


def build_obj_list(num_array: np.ndarray) -> list:
    rows, cols = num_array.shape[0], num_array.shape[1]
    obj_list = []
    for x in range(0, rows):
        for y in range(0, cols):
            if (x == 0) and (y == 0):
                # first position can only have down and right
                obj_list.append(Position(num_array[x, y], None, num_array[x + 1, y], None, num_array[x, y + 1]))
            elif (x == 0) and (y == cols-1):
                # first row after last column can only have down and left
                obj_list.append(Position(num_array[x, y], None, num_array[x + 1, y], num_array[x, y - 1], None))
            elif (x == rows-1) and (y == 0):
                # last row first column can only have up and right
                obj_list.append(Position(num_array[x, y], num_array[x - 1, y], None, None, num_array[x, y - 1]))
            elif (x == rows-1) and (y == cols-1):
                # last row last column can only have up and left
                obj_list.append(Position(num_array[x, y], num_array[x - 1, y], None, num_array[x, y - 1], None))
            elif y == 0:
                # middle rows first column can only have up, down and right
                obj_list.append(Position(num_array[x, y], num_array[x - 1, y], num_array[x + 1, y], None, num_array[x, y + 1]))
            elif y == cols-1:
                # middle rows last column can only have up, down and left
                obj_list.append(Position(num_array[x, y], num_array[x - 1, y], num_array[x + 1, y], num_array[x, y - 1], None))
            elif x == 0:
                # middle columns first row can only have down, left and right
                obj_list.append(Position(num_array[x, y], None, num_array[x + 1, y], num_array[x, y - 1], num_array[x, y + 1]))
            elif x == rows-1:
                # middle columns last row can only have up, left and right
                obj_list.append(Position(num_array[x, y], num_array[x - 1, y], None, num_array[x, y - 1], num_array[x, y + 1]))
            else:
                # other rows
                obj_list.append(Position(num_array[x, y], num_array[x - 1, y], num_array[x + 1, y], num_array[x, y - 1], num_array[x, y + 1]))

    return obj_list


def check_heights(obj_list: list):
    return [position.pos + 1 for position in obj_list if position.is_low()]


def main():
    nums = read_file('AoC_9.txt')
    # test:
    # num_array = to_array(nums, 5, 10)
    # actual
    num_array = to_array(nums, 100, 100)

    obj_list = build_obj_list(num_array)
    risk_levels = check_heights(obj_list)
    print(sum(risk_levels))


if __name__ == '__main__':
    main()
