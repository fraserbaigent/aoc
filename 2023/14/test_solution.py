import copy
import solution

test_data = [l.strip() for l in '''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.split('\n') if len(l.strip())]

test_data_ = [l.strip() for l in '''
####
#..#
#O.#
####
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 136
    assert solution.part_1(copy.deepcopy(test_data), False) == expected_part_1

def test_part_2():
    expected_part_2 = 64
    assert solution.part_2(copy.deepcopy(test_data), False) == expected_part_2

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
    assert solution.rotate(curr, 'S') == pos_3    
    curr = copy.deepcopy(pos_1)
    assert solution.rotate(curr, 'S') == pos_4
    curr = copy.deepcopy(pos_1)

def test_rotate_test_data():
    raw_data = [
        ['O','O','O','O','.','#','.','O','.','.',],
        ['O','O','.','.','#','.','.','.','.','#',],
        ['O','O','.','.','O','#','#','.','.','O',],
        ['O','.','.','#','.','O','O','.','.','.',],
        ['.','.','.','.','.','.','.','.','#','.',],
        ['.','.','#','.','.','.','.','#','.','#',],
        ['.','.','O','.','.','#','.','O','.','O',],
        ['.','.','O','.','.','.','.','.','.','.',],
        ['#','.','.','.','.','#','#','#','.','.',],
        ['#','.','.','.','.','#','.','.','.','.',],
        ]
    after_e = [
        ['.','O','O','O','O','#','.','.','.','O',],
        ['.','.','O','O','#','.','.','.','.','#',],
        ['.','.','O','O','O','#','#','.','.','O',],
        ['.','.','O','#','.','.','.','.','O','O',],
        ['.','.','.','.','.','.','.','.','#','.',],
        ['.','.','#','.','.','.','.','#','.','#',],
        ['.','.','.','.','O','#','.','.','O','O',],
        ['.','.','.','.','.','.','.','.','.','O',],
        ['#','.','.','.','.','#','#','#','.','.',],
        ['#','.','.','.','.','#','.','.','.','.',],
        ]
    
    assert solution.rotate(copy.deepcopy(raw_data), 'E') == after_e
    after_s = [
        ['.','.','.','.','.','#','.','.','.','.',],
        ['.','.','.','.','#','.','.','.','.','#',],
        ['.','.','.','O','.','#','#','.','.','.',],
        ['.','.','.','#','.','.','.','.','.','.',],
        ['O','.','O','.','.','.','.','O','#','O',],
        ['O','.','#','.','.','O','.','#','.','#',],
        ['O','.','.','.','.','#','.','.','.','.',],
        ['O','O','.','.','.','.','O','O','.','.',],
        ['#','O','O','.','.','#','#','#','.','.',],
        ['#','O','O','.','O','#','.','.','.','O',],
        ]
    assert solution.rotate(copy.deepcopy(raw_data), 'S') == after_s
    after_w = [
        ['O','O','O','O','.','#','O','.','.','.',],
        ['O','O','.','.','#','.','.','.','.','#',],
        ['O','O','O','.','.','#','#','O','.','.',],
        ['O','.','.','#','O','O','.','.','.','.',],
        ['.','.','.','.','.','.','.','.','#','.',],
        ['.','.','#','.','.','.','.','#','.','#',],
        ['O','.','.','.','.','#','O','O','.','.',],
        ['O','.','.','.','.','.','.','.','.','.',],
        ['#','.','.','.','.','#','#','#','.','.',],
        ['#','.','.','.','.','#','.','.','.','.',],
    ]
    actual = solution.rotate(copy.deepcopy(raw_data), 'W')
    assert actual == after_w    
    after_n = [
        ['O','O','O','O','.','#','.','O','.','.',],
        ['O','O','.','.','#','.','.','.','.','#',],
        ['O','O','.','.','O','#','#','.','.','O',],
        ['O','.','.','#','.','O','O','.','.','.',],
        ['.','.','.','.','.','.','.','.','#','.',],
        ['.','.','#','.','.','.','.','#','.','#',],
        ['.','.','O','.','.','#','.','O','.','O',],
        ['.','.','O','.','.','.','.','.','.','.',],
        ['#','.','.','.','.','#','#','#','.','.',],
        ['#','.','.','.','.','#','.','.','.','.',],
        ]
    assert solution.rotate(copy.deepcopy(raw_data), 'N') == after_n
    
def test_no_extra_boulders():
    data = []
    for d in test_data:
        data.append([i for i in d])
    directions = ['N','W','S','E',]
    for i in range(0,1000):
        data = solution.rotate(data, directions[i%4])
        total=0
        for r in data:
            total += sum([1 for i in r if i == 'O'])
        for r in data:
            print(''.join(r))
        print(f'Rotated after step {i} - total = {total} from a {directions[i%4]} rotation.')
        
            
        if total != 18:
            print(i)
        assert total == 18

def test_cache_works():
    data = []
    for d in test_data:
        data.append([i for i in d])
    data_copy = copy.deepcopy(data)
    directions = ['N','W','S','E',]
    times_to_rotate = 1000
    for i in range(0,4*times_to_rotate):
        data = solution.rotate(data, directions[i%4])
    adjusted = solution.adjust_data(data_copy, times_to_rotate)

    assert adjusted == data

def test_rotate_cycles_2():
    dirs = ['N','W','S','E']
    first = solution.data_to_matrix('''.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....'''.split("\n"))
    dat = solution.data_to_matrix(copy.deepcopy(test_data))
    for c in dirs:
        solution.rotate(dat, c)
    assert dat == first
    
    second=solution.data_to_matrix('''.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O'''.split("\n"))
    for c in dirs:
        solution.rotate(dat, c)
    assert dat == second
    
    third=solution.data_to_matrix('''.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O'''.split("\n"))
    for c in dirs:
        solution.rotate(dat, c)
    assert dat == third    
