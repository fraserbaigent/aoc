import solution
test_data = [l.strip() for l in '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 161
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 48
    data_2= ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    assert solution.part_2(data_2) == expected_part_2
