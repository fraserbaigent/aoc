def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(line):
    return [int(i.strip()) for i in line.split()]


def get_prediction(readings: list):
    next_readings = list()
    for i in range(0, len(readings) - 1):
        next_readings.append(readings[i + 1] - readings[i])
    all_zeroes = True
    for i in next_readings:
        if i != 0:
            all_zeroes = False
            break

    if all_zeroes:
        next_readings.append(0)
    else:
        next_readings.append(get_prediction(next_readings))

    to_append = next_readings[-1] + readings[-1]
    readings.append(to_append)
    return readings[-1]


def get_prediction_2(readings: list):
    next_readings = list()
    for i in range(0, len(readings) - 1):
        next_readings.append(readings[i + 1] - readings[i])
    all_zeroes = True
    for i in next_readings:
        if i != 0:
            all_zeroes = False
            break

    if all_zeroes:
        next_readings = [0] + next_readings
    else:
        next_readings = [get_prediction_2(next_readings)] + next_readings

    return readings[0] - next_readings[0]


def part_1(data):
    total = 0
    for d in data:
        readings = parse_data(d)
        total += get_prediction(readings)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    for d in data:
        readings = parse_data(d)
        total += get_prediction_2(readings)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
