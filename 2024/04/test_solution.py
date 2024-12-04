import solution
from AocCommon import data_to_list_grid, get_data

test_data = data_to_list_grid([l.strip() for l in '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''.split('\n') if len(l.strip())])

def test_part_1():
    expected_part_1 = 18
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 9
    assert solution.part_2(test_data) == expected_part_2
