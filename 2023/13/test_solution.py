import solution

test_data = [
    l.strip()
    for l in """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.


#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

.####.##.####..
.#..##..##..#.#
.#..##..##..#..
.####.##.####..
.#.#.####.#.#.#
.##.#....#.##..
.#.##.##.##.#.#
##..#.##.#..###
...###..###....
.....####.....#
###.#.##.#.####
...#..##..#....
##..........###

##..###.#.#
##...##.#.#
##.#.#.#..#
..#..#.###.
##.##.##.#.
#####.....#
##.#.......
....##..##.
##..###.#..
......#.##.
##.###.#...

.#..#.#..
#.#...#..
#.....#..
....#####
#.####.#.
#.####.#.
....#####
#.....#..
#.#...#..

.#..##..##.
.#.#.#.####
#.####.##.#
####.######
..###...##.
#.#########
..#.##.####
#.#..#.#..#
#.#..######
####.#.####
####.#.####
#.#..######
#.#..#.#..#             
""".split(
        "\n"
    )
]


def test_part_1():
    expected_part_1 = 913
    assert solution.part_1(test_data) == expected_part_1


def test_part_2():
    expected_part_2 = 400
    assert solution.part_2(test_data) == expected_part_2


def test_parse_data():
    expected = [
        [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ],
        [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#",
        ],
        [
            ".####.##.####..",
            ".#..##..##..#.#",
            ".#..##..##..#..",
            ".####.##.####..",
            ".#.#.####.#.#.#",
            ".##.#....#.##..",
            ".#.##.##.##.#.#",
            "##..#.##.#..###",
            "...###..###....",
            ".....####.....#",
            "###.#.##.#.####",
            "...#..##..#....",
            "##..........###",
        ],
        [
            "##..###.#.#",
            "##...##.#.#",
            "##.#.#.#..#",
            "..#..#.###.",
            "##.##.##.#.",
            "#####.....#",
            "##.#.......",
            "....##..##.",
            "##..###.#..",
            "......#.##.",
            "##.###.#...",
        ],
        [
            ".#..#.#..",
            "#.#...#..",
            "#.....#..",
            "....#####",
            "#.####.#.",
            "#.####.#.",
            "....#####",
            "#.....#..",
            "#.#...#..",
        ],
        [
           ".#..##..##.",
         ".#.#.#.####",
         "#.####.##.#",
         "####.######",
         "..###...##.",
         "#.#########",
         "..#.##.####",
         "#.#..#.#..#",
         "#.#..######",
         "####.#.####",
         "####.#.####",
         "#.#..######",
         "#.#..#.#..#",
        ],
    ]
    assert solution.parse_data(test_data) == expected

def test_get_vertical_score():
    patterns = solution.parse_data(test_data)

    assert solution.get_vertical_score(patterns[0]) == 5
    assert solution.get_vertical_score(patterns[1]) == 0
    assert solution.get_vertical_score(patterns[2]) == 7
    assert solution.get_vertical_score(patterns[3]) == 1
    assert solution.get_vertical_score(patterns[4]) == 0
    assert solution.get_vertical_score(patterns[5]) == 0


def test_get_horizontal_score():
    patterns = solution.parse_data(test_data)

    assert solution.get_horizontal_score(patterns[0]) == 0
    assert solution.get_horizontal_score(patterns[1]) == 4
    assert solution.get_horizontal_score(patterns[2]) == 0
    assert solution.get_horizontal_score(patterns[3]) == 0
    assert solution.get_horizontal_score(patterns[4]) == 500
    assert solution.get_horizontal_score(patterns[5]) == 1000

def test_in_prod():
    patterns = solution.parse_data(solution.data)

    expected = {
        94: [0, 2],
        95: [2, 0],
        96: [5, 0],
        97: [0, 1],
        98: [14, 0],
        99: [0, 7],
    }
    for i, p in enumerate(patterns):
        if i in expected:
            assert solution.get_horizontal_score(p) == expected[i][0]
            assert solution.get_vertical_score(p) == expected[i][1]


def test_my_pattern():
    pattern = [
        "#..#.#...#.#..##",
        "#.##.#...##...##",
        "##.#.#..#.#..###",
        "#.###...#.##..##",
    ]
    assert solution.get_horizontal_score(pattern) == 0
    assert solution.get_vertical_score(pattern) == 15


def test_my_second_pattern():
    pattern = [
        "##..#.#...#.#...#",
        "##.##.#...##...##",
        "###.#.#..#.#..##.",
        "##.###...#.##..##",
    ]
    assert solution.get_horizontal_score(pattern) == 0
    assert solution.get_vertical_score(pattern) == 1


def test_my_part_2():
    pattern = [
        [d_i for d_i in d]
        for d in [
            "###.#....",
            "..#.#....",
            "..##.###.",
            "..##.###.",
            "..#.#....",
            "###.#....",
            "...#..##.",
            "###...#.#",
            ".##..####",
            ".##..####",
            ".##...#.#",
            "...#..##.",
            "###.#....",
            "..#.#....",
            "..##.###.",
        ]
    ]

    fixed_pattern = [
        [d_i for d_i in d]
        for d in [
            "###.#....",
            "..#.#....",
            "..##.###.",
            "..##.###.",
            "..#.#....",
            "###.#....",
            "...#..##.",
            "###...#.#",
            ".##..####",
            ".##..####",
            "###...#.#",
            "...#..##.",
            "###.#....",
            "..#.#....",
            "..##.###.",
        ]
    ]
    assert solution.get_horizontal_score(pattern) == 3
    assert solution.get_horizontal_score(fixed_pattern, [3]) == 9
    for i, p in enumerate(patterns):
        if i in expected:
            assert solution.get_horizontal_score(p) == expected[i][0]
            assert solution.get_vertical_score(p) == expected[i][1]            
        

    
def test_my_pattern():
    pattern = [
        '#..#.#...#.#..##',
        '#.##.#...##...##',
        '##.#.#..#.#..###',
        '#.###...#.##..##',
        ]
    assert solution.get_horizontal_score(pattern) == 0
    assert solution.get_vertical_score(pattern) == 15

def test_my_second_pattern():
    pattern = [
        '##..#.#...#.#...#',
        '##.##.#...##...##',
        '###.#.#..#.#..##.',
        '##.###...#.##..##',
        ]
    assert solution.get_horizontal_score(pattern) == 0
    assert solution.get_vertical_score(pattern) == 1
    
def test_my_part_2():
    pattern = [[d_i for d_i in d] for d in [       
'###.#....',
'..#.#....',
'..##.###.',
'..##.###.',
'..#.#....',
'###.#....',
'...#..##.',
'###...#.#',
'.##..####',
'.##..####',
'.##...#.#',
'...#..##.',
'###.#....',
'..#.#....',
'..##.###.',
        ]]

    fixed_pattern = [[d_i for d_i in d] for d in [       
'###.#....',
'..#.#....',
'..##.###.',
'..##.###.',
'..#.#....',
'###.#....',
'...#..##.',
'###...#.#',
'.##..####',
'.##..####',
'###...#.#',
'...#..##.',
'###.#....',
'..#.#....',
'..##.###.',
        ]]
    assert solution.get_horizontal_score(pattern) == 3
    assert solution.get_horizontal_score(fixed_pattern, [3]) == 9
