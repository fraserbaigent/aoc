import copy

from AocCommon import get_data_blob

data = get_data_blob()

##########################################################################


def parse(data):
    files = []
    total = 0
    file_index = 0
    for index, i in enumerate(data.strip()):
        files.append(
            {
                "file_index": file_index if index % 2 == 0 else -1,
                "width": int(i),
            }
        )
        total += int(i)
        if index % 2:
            file_index += 1

    return files


def solve_part_1(data):
    files = parse(data)
    file_index = len(files) - 1

    left_i = 0
    right_i = len(files) - 1
    while left_i < right_i:
        while files[left_i]["file_index"] >= 0:
            left_i += 1
        while files[right_i]["file_index"] < 0:
            right_i -= 1
        if left_i >= right_i:
            break
        right_file = files[right_i]
        empty = files[left_i]
        val_to_fill = right_file["file_index"]
        if files[left_i - 1]["file_index"] != val_to_fill:
            new_file = {
                "file_index": val_to_fill,
                "width": 0,
            }
            files.insert(left_i, new_file)
            left_i += 1
            right_i += 1
        file = files[left_i - 1]
        delta = min(right_file["width"], empty["width"])
        file["width"] += delta
        right_file["width"] -= delta
        empty["width"] -= delta
        if right_file["width"] < 0:
            raise Exception(f"File {right_file} has invalid width")
        if empty["width"] < 0:
            raise Exception(f"EmptyFile {empty} has invalid width")

        if right_file["width"] == 0:
            del files[right_i]
            right_i -= 1
        if empty["width"] == 0:
            files.remove(empty)
            right_i -= 1

    total = 0
    index = 0
    for f in files:
        for i in range(f["width"]):
            total += max(0, f["file_index"]) * index
            index += 1
    return total


def solve_part_2(data):
    files = parse(data)
    file_index = len(files) - 1

    right_i = len(files) - 1
    moved_indices = set()
    while right_i >= 0:
        while files[right_i]["file_index"] < 0:
            right_i -= 1
        right_file = files[right_i]
        if right_file["file_index"] in moved_indices:
            right_i -= 1
            continue
        for i, f in enumerate(files):
            if i >= right_i:
                break
            empty = files[i]
            if empty["file_index"] >= 0:
                continue

            if empty["width"] < right_file["width"]:
                continue
            elif empty["width"] == right_file["width"]:
                moved_indices.add(right_file["file_index"])
                empty["file_index"] = right_file["file_index"]
                right_file["file_index"] = -1
                right_i -= 1
                break
            else:
                moved_indices.add(right_file["file_index"])
                new_file = copy.deepcopy(right_file)
                empty["width"] -= new_file["width"]
                files.insert(i, new_file)
                right_file["file_index"] = -1
                break

        moved_indices.add(right_file["file_index"])

    total = 0
    index = 0
    for f in files:
        for i in range(f["width"]):
            total += max(0, f["file_index"]) * index
            index += 1
    return total


def part_1(data):
    total = solve_part_1(data)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = solve_part_2(data)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
