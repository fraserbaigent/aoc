def get_test_data(test_str):
    return [
        [int(i) if i != '.' else None for i in d] for d in 
        test_str.split("\n")]    
import solution

test_data = get_test_data(
'''...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9''')

test_data_2 = get_test_data(
'''..90..9
...1.98
...2..7
6543456
765.987
876....
987....''')

test_data_3 = get_test_data(
'''10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01''')

test_data_4 = get_test_data(
    '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732''')

def test_part_1():
    expected_part_1 = 2
    assert solution.part_1(test_data) == expected_part_1

def test_part_12():
    expected_part_1 = 4
    assert solution.part_1(test_data_2) == expected_part_1

def test_part_13():
    expected_part_1 = 3
    assert solution.part_1(test_data_3) == expected_part_1

def test_part_14():
    expected_part_1 = 36
    assert solution.part_1(test_data_4) == expected_part_1


def test_part_2():
    expected_part_2 = None
    assert solution.part_2(test_data) == expected_part_2
