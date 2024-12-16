from AocCommon import data_to_list_grid
import solution
test_data = [l.strip() for l in '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''.split('\n') if len(l.strip())]
test_data = data_to_list_grid(test_data)
def test_part_1():
    expected_part_1 = 7036
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 45
    assert solution.part_2(test_data) == expected_part_2
