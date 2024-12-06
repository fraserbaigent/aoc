import solution
test_data = [l.strip() for l in '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47                                
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 143
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 123
    assert solution.part_2(test_data) == expected_part_2
