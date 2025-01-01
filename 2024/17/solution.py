import math


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def solve_part_1(a, b, c, commands):
    index = 0
    outputs = list()
    iterations = 0
    while index < len(commands):  # and iterations < 1e7:
        increase = True
        ins = commands[index]
        op = commands[index + 1]
        if op <= 3:
            v = op
        elif op == 4:
            v = a
        elif op == 5:
            v = b
        elif op == 6:
            v = c
        elif op == 7:
            v = None

        if ins == 0:
            a = int(math.trunc(a / float(2**v)))
        elif ins == 1:
            b = int(b) ^ op
        elif ins == 2:
            b = v % 8
        elif ins == 3:
            if a != 0:
                index = op
                increase = False
        elif ins == 4:
            b = b ^ c
        elif ins == 5:
            outputs.append(v % 8)
        elif ins == 6:
            b = int(math.trunc(a / (2.0**v)))
        elif ins == 7:
            c = int(math.trunc(a / (2.0**v)))

        if increase:
            index += 2
        iterations += 1

    return outputs


def solve_part_2(input_commands):
    a = 50230824
    ind = 0
    longest = 0
    matched = list()
    while True:
        outputs = solve_part_1(a, 0, 0, input_commands)
        a = int(a)
        if len(outputs) < len(input_commands):
            a *= 8
        elif len(outputs) > len(input_commands):
            a /= 8
        else:
            a += int(int(a) // 8)

        if len(outputs) == len(input_commands):
            p = len(matched)
            m = 0
            for i in range(len(input_commands)):
                index = len(outputs) - 1 - i
                if outputs[index] == input_commands[index]:
                    m += 1
                else:
                    break
            if m > 0:
                matched.append((a, m))
            if len(matched) > p:
                print(
                    f"{a:<15} ({a %
                                8}): {matched[-1]} matched:\n{outputs}\n{input_commands}"
                )
                ind += 1

        #        print(",".join([str(o) for o in input_commands]))
        #        print(",".join([str(o) for o in outputs]))
        if outputs == input_commands or ind >= 10:
            break
    matched = sorted(matched, key=lambda k: k[0])
    for i in range(1, len(matched)):
        m, l = matched[i]
        delta = m - matched[i - 1][0]
        print(m, l, delta)

    return a


def part_1(data):
    a = int(data[0].split(":")[-1])
    b = int(data[1].split(":")[-1])
    c = int(data[2].split(":")[-1])
    commands = [int(i) for i in data[-1].split(":")[1].split(",")]

    outputs = solve_part_1(a, b, c, commands)
    answer = ",".join([str(i) for i in outputs])
    print(f"Part 1: {answer}")


def part_2(data):
    commands = [int(i) for i in data[-1].split(":")[1].split(",")]
    total = solve_part_2(commands)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
