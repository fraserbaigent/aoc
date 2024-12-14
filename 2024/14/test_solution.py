from AocCommon import split_data_with_regex
import solution
test_data = [l.strip() for l in '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''.split('\n') if len(l.strip())]
test_data = split_data_with_regex(
    test_data, "p=(.*),(.*) v=(.*),(.*)", types=[int, int, int, int]
    )
X_LIM = 11
Y_LIM = 7

def test_part_1():
    expected_part_1 = 12
    assert solution.solve_part_1(test_data,100,11,7) == expected_part_1
