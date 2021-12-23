
import statistics

def read_file(fname: str) -> list:
    file = open(fname, 'r')
    file_str = [line.split(',') for line in file][0]
    file_int = [int(char) for char in file_str]
    return file_int


def calc_differences(pos_list: list, median: int) -> int:
    fuel_sum = 0
    for i in pos_list:
        fuel_sum += abs(i - median)
    return fuel_sum

def main():
    positions = read_file('AoC_7.txt')
    median_val = int(statistics.median(positions))
    fuel_sum = calc_differences(positions, median_val)
    print(fuel_sum)

if __name__ == '__main__':
    main()
