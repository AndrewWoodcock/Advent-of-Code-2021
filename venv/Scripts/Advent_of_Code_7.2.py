
import statistics

def read_file(fname: str) -> list:
    file = open(fname, 'r')
    file_str = [line.split(',') for line in file][0]
    file_int = [int(char) for char in file_str]
    return file_int


def calculate_fuel(positions_list: list, mean_list:list) -> int:
    fuel_cost = 0
    min_fuel = 9999999999999
    for val in mean_list:
        for element in positions_list:
            n = abs(element - val)
            # n2/2 + n/2
            fuel_used = ((n**2)/2) + n/2
            fuel_cost += fuel_used
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost
    return min_fuel


def main():
    positions = read_file('AoC_7.txt')
    mean_val = round(statistics.mean(positions))
    mean_list = [mean_val -1, mean_val, mean_val + 1]
    total_fuel_cost = calculate_fuel(positions, mean_list)
    print(round(total_fuel_cost))


if __name__ == '__main__':
    main()

# n2/2 + n/2