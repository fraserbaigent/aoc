import solution
test_data = [l.strip() for l in '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''.split('\n')]

def test_part_1():
    expected_part_1 = 6
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 16
    assert solution.part_2(test_data) == expected_part_2
