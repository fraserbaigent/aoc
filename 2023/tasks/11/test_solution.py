import solution
test_data = [l.strip() for l in '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 374
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 8410
    multiplier=100
    assert solution.part_2(test_data, multiplier) == expected_part_2

    expected_part_2 = 1030
    multiplier=10
    assert solution.part_2(test_data, multiplier) == expected_part_2


def get_distance_between():
    pair = ([0,1],[5,5])
    assert solution.get_distance_between(pair) == 9

def test_parse_map():
    result = solution.parse_map(test_data)
    expected = ([[0,3],[1,7],[2,0],[4,6],[5,1],[6,9],[8,7],[9,0],[9,4]],
        [3,7],
        [2,5,8])
    assert expected == result

def test_get_galaxy_coordinates():
    result = solution.get_galaxy_coordinates(test_data, 10)
    expected = [[0,12],[1,25],[2,0],[13,24],[14,1],[15,36],[26,25],[27,0],[27,13]]
    assert expected==result
