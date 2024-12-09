import solution
test_data = "2333133121414131402"

def test_part_1():
    expected_part_1 = 1928
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 2858
    assert solution.part_2(test_data) == expected_part_2
