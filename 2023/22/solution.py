import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")
CHAR_ZERO = "0"
##########################################################################


class Brick:
    def __init__(self, index, x0, y0, z0, x1, y1, z1):
        self.index = index
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

        self.children = list()
        self.parents = list()

    def add_child(self, other):
        self.children.append(other)

    def add_parent(self, other):
        self.parents.append(other)

    def print(self):
        print(f"({self.x0}, {self.y0}, {self.z0}), ({self.x1}, {self.y1}, {self.z1})")

    def coord(self):
        return f"{self.x0}, {self.y0}, {self.x1}, {self.y1}"


def intersects(x00, x01, x10, x11):
    if x10 > x01:
        return False
    elif x11 < x00:
        return False
    return True


def print_intersecting_lines(x00, y00, x01, y01, x10, y10, x11, y11):
    min_x = min([x00, x01, x10, x11])
    max_x = max([x00, x01, x10, x11])
    min_y = min([y00, y01, y10, y11])
    max_y = max([y00, y01, y10, y11])

    g = [
        [" " for _ in range(0, max_x - min_x + 1)] for _ in range(0, max_y - min_y + 1)
    ]
    for x in range(x00 - min_x, x01 - min_x + 1):
        for y in range(y00 - min_y, y01 - min_y + 1):
            g[y][x] = "O"
    for x in range(x10 - min_x, x11 - min_x + 1):
        for y in range(y10 - min_y, y11 - min_y + 1):
            if g[y][x] == "O":
                g[y][x] = "X"
            else:
                g[y][x] = "#"

    print("\n".join([" ".join(g_) for g_ in g]))


def parse_data(data):
    rx = re.compile("(\\d+),(\\d+),(\\d+)\\~(\\d+),(\\d+),(\\d+)$")
    root = Brick(CHAR_ZERO, 0, 0, 0, 0, 0, 0)
    bricks = [root]
    split_data = list()
    for d in data:
        res = rx.match(d)
        split_data.append(tuple([int(r_i) for r_i in res.groups()]))
    split_data = sorted(split_data, key=lambda k: k[2])

    for g in split_data:
        for i in range(len(bricks) - 1, -1, -1):
            x0, y0, z0, x1, y1, z1 = g
            that_brick = bricks[i]
            if that_brick.z0 == 0 or (
                intersects(x0, x1, that_brick.x0, that_brick.x1)
                and intersects(y0, y1, that_brick.y0, that_brick.y1)
            ):
                dz = z1 - z0
                z0n = that_brick.z1 + 1
                z1n = z0n + dz

                new_brick = Brick(
                    chr(ord("A") + -1 + len(bricks)), x0, y0, z0n, x1, y1, z1n
                )

                for b in bricks:
                    if b.z1 == new_brick.z0 - 1 and (
                        b.index == CHAR_ZERO
                        or (
                            intersects(x0, x1, b.x0, b.x1)
                            and intersects(y0, y1, b.y0, b.y1)
                        )
                    ):
                        b.add_child(new_brick)
                        new_brick.add_parent(b)

                bricks.append(new_brick)
                bricks = sorted(bricks, key=lambda k: k.z1)
                break
    return root, bricks


def recurse(root, visited, can_delete):
    if root.index in visited:
        return

    visited.add(root.index)
    if len(root.children) == 0:
        can_delete.add(root.index)
    else:
        can_add = True
        for c in root.children:
            if len(c.parents) == 1:
                can_add = False
                break
        if can_add:
            can_delete.add(root.index)

    for c in root.children:
        recurse(c, visited, can_delete)


def find_total_safe(root):
    can_delete = set()
    visited = set()

    recurse(root, visited, can_delete)

    return len(can_delete)


def disintegrate_above(brick):
    fallen_bricks = set()
    tried_bricks = set()
    bricks_to_try = [b for b in brick.children]
    while len(bricks_to_try) > 0:
        this_brick = bricks_to_try.pop(0)
        if this_brick.index in tried_bricks:
            continue

        tried_bricks.add(this_brick.index)
        will_fall = True
        for p in this_brick.parents:
            if p.index != brick.index and p.index not in fallen_bricks:
                will_fall = False
                break

        if not will_fall:
            continue

        fallen_bricks.add(this_brick.index)
        bricks_to_try += this_brick.children

        bricks_to_try = sorted(bricks_to_try, key=lambda b: brick.z0)

    return len(fallen_bricks)


def print_grid(bricks):
    max_x = min_x = max_z = min_z = None
    for b in bricks:
        if max_x is None or max_x < b.x1:
            max_x = b.x1
        if min_x is None or min_x > b.x0:
            min_x = b.x0
        if max_z is None or max_z < b.z1:
            max_z = b.z1
        if min_z is None or min_z > b.z0:
            min_z = b.z0
    grid = [
        [" " for _ in range(0, max_x - min_x + 1)] for z in range(0, max_z - min_z + 1)
    ]
    grid.append(["_" for i in range(0, len(grid[0]))])
    for b in bricks:
        if b.index == CHAR_ZERO:
            continue
        for x in range(b.x0, b.x1 + 1):
            for z in range(b.z0, b.z1 + 1):
                z_c = len(grid) - 1 - z
                if grid[z_c][x] == " ":
                    grid[z_c][x] = b.index
                else:
                    grid[z_c][x] = "?"

    print(
        "\n".join([f"{len(grid) - i-1 :<3} " + " ".join(g) for i, g in enumerate(grid)])
    )


def part_1(data):
    root, bricks = parse_data(data)
    total = find_total_safe(root)

    print(f"Part 1: {total}")
    return total


def part_2(data):
    root, bricks = parse_data(data)
    print_grid(bricks)
    total = 0
    for b in bricks:
        if b.index == CHAR_ZERO:
            continue
        disintegrated_count = disintegrate_above(b)
        total += disintegrated_count
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
