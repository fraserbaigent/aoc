import solution
test_data = [l.strip() for l in '''
R 9 (#70c710)
D 6 (#0dc571)
L 2 (#5713f0)
U 2 (#5713f0)
L 3 (#5713f0)                                
D 4 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 3 (#7a21e3)
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = [10,10,10,10,8,6,8,5,7,6,6]
    result = solution.part_1(test_data)
    i=0
    for e, r in zip(expected_part_1, result):
        
        if e != r:
            print(f'{i:>2}: {e} not found - got {r}')
        i+=1
    assert expected_part_1 == result

def test_part_2():
    expected_part_2 = 0
    assert solution.part_2(test_data) == expected_part_2

def test_parse_data():
    expected = [
        ['R', 9 ,'70c710'],
        ['D', 6 ,'0dc571'],
        ['L', 2 ,'5713f0'],
        ]
    
    assert expected== solution.parse_data(test_data[:3])

def test_get_lines():
    parsed = [
        ['R', 9 ,'70c710'],
        ['D', 6 ,'0dc571'],
        ['L', 2 ,'5713f0'],
        ['D', 2 ,'d2c081'],
        ]
    

    expected = [
        [[0,0],[9,0],'70c710'],
        [[9,0],[9,6],'0dc571'],
        [[9,6],[7,6],'5713f0'],
        [[7,6],[7,8],'d2c081'],
        ]
    
    assert expected== solution.get_lines(parsed)

def test_get_vertical_lines():
    lines = [
        [[0,0],[6,0],'70c710'],
        [[6,0],[6,5],'0dc571'],
        [[6,5],[4,5],'5713f0'],
        [[4,5],[4,7],'d2c081'],
        ]

    expected = ([
        [[6,0],[6,5],'0dc571'],
        [[4,5],[4,7],'d2c081'],
        ],
        0,7,
        {
         (4,5): (6,5),
         (0,0):(6,0),
                })

    assert expected == solution.get_vertical_lines(lines)
    

def test_sort_lines():
    lines = [
        [[6.7],[6,12],'abcde0'],
        [[6,0],[6,5],'0dc571'],
        [[4,5],[4,7],'d2c081'],
        [[6, -1], [6, -3], '2f9f73'],
        [[3, -3], [3, -6], '450603'],
        [[-3, -6], [-3, -11], '4a2f93'],
        [[-12, -11], [-12, -15], '132a73'],
        [[-7, -15], [-7, -18], '2846e3'],
        [[-4, -18], [-4, -28], '087b73'],
        ]


    expected = [
        [[-12, -11], [-12, -15], '132a73'],
        [[-7, -15], [-7, -18], '2846e3'],
        [[-4, -18], [-4, -28], '087b73'],
        [[-3, -6], [-3, -11], '4a2f93'],
        [[3, -3], [3, -6], '450603'],
        [[4,5],[4,7],'d2c081'],
        [[6, -1], [6, -3], '2f9f73'],
        [[6,0],[6,5],'0dc571'],
        [[6.7],[6,12],'abcde0'],
        ]

    assert expected == solution.sort_vlines(lines)


def test_complex_test_1():
    new_test_data = [l.strip() for l in '''
R 10 (#70c710)
U 4 (#0dc571)
L 2 (#5713f0)
D 10 (#5713f0)
L 1 (#5713f0)
U 4 (#5713f0)
L 3 (#5713f0)                                                                                                                
D 4 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 2 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''.split('\n') if len(l.strip())]

    '''
0                   # # # 3
1                   #   # 3
2                   #   # 3
3                   #   # 3
4   # # # # # # # # # # # 11
5   #               #     9
6   # # #   # # # # #     9
7       #   #     # #     5
8   # # #   #     # #     7
9   #       #     # #     7
10  # #     # # # # #     9
11    #         #         6
12    # # # # # #         6
'''
    result = solution.part_1(new_test_data)
    assert result == [3,3,3,3,11,9,9,5,7,7,9,6,6]
