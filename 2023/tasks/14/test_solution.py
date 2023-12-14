import copy
import solution
test_data = [l.strip() for l in '''
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
'''.split('\n') if len(l.strip())]

test_data_ = [l.strip() for l in '''
####
#..#
#O.#
####
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 136
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 64
    assert solution.part_2(test_data) == expected_part_2

def test_part_2_cache():
    pos_0 = [
"####",
"#..#",
"#.O#",
"####",
        ]
    pos_1 = [
"####",
"#.O#",
"#..#",
"####",
        ]
    pos_2 = [
"####",
"#O.#",
"#..#",
"####",
        ]
    pos_3 = [
"####",
"#..#",
"#O.#",
"####",
        ]
    pos_4 = [
"####",
"#..#",
"#.O#",
"####",
        ]
    cache_ref = dict()
    cache_ref[1] = pos_1
    cache_ref[2] = pos_2
    cache_ref[3] = pos_3
    cache_ref[4] = pos_4
    
    data_cache = {
        hash(('N', *pos_1)):1,
        hash(('W', *pos_2)):2,
        hash(('S', *pos_3)):3,
        hash(('E', *pos_4)):4,
        }

    next_step = hash(('N', *pos_1))
    expected_end = solution.lookup_from_cache(5,data_cache,cache_ref, next_step, 8)
    assert expected_end == (8, pos_4)
    
def test_get_score_for_line():
    lines = [
        [[[0,4]], 34],
        [[[0,3]], 27 ],
        [[[0,1],[6,2]],17],
        ]
    for l in lines:
        assert solution.get_scores_for_lines(l[0], 10) == l[1]
    
    
def test_rotate():
    pos_1 = [
        ["#","#","#","#"],
    ["#",".","O","#"],
    ["#",".",".","#"],
    ["#","#","#","#"],
    ]
    pos_2 = [
    ["#","#","#","#"],
    ["#","O",".","#"],
    ["#",".",".","#"],
    ["#","#","#","#"],
    ]
    pos_3 = [
    ["#","#","#","#"],
    ["#",".",".","#"],
    ["#","O",".","#"],
    ["#","#","#","#"],
        ]
    pos_4 = [
        ["#","#","#","#"],
    ["#",".",".","#"],
    ["#",".","O","#"],
    ["#","#","#","#"],
        ]
    curr = copy.deepcopy(pos_1)
    assert solution.rotate(curr,'E') == pos_1
    assert solution.rotate(curr,'N') == pos_1
    assert solution.rotate(curr, 'W') == pos_2
    curr = copy.deepcopy(pos_1)
    assert solution.rotate(curr, 'S') == pos_4
    curr = copy.deepcopy(pos_1)
