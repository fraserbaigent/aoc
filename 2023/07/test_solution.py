import solution
test_data = [l.strip() for l in '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 6440
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 5905
    assert solution.part_2(test_data) == expected_part_2
