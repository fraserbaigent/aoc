import solution
test_data = [l.strip() for l in '''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 21
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 525152
    assert solution.part_2(test_data) == expected_part_2

def test_parse_data():
    expected = [
        ['???.###',[1,1,3]],
        ['.??..??...?##.',[1,1,3]],
        ['?#?#?#?#?#?#?#?', [1,3,1,6]],
        ['????.#...#...', [4,1,1]],
        ['????.######..#####.', [1,6,5]],
        ['?###????????', [3,2,1]],
        ]
    assert solution.parse_data(test_data) == expected

def test_recurse():
    cases =[
        ['???.###',[1,1,3],1],
        ['.??..??...?##.',[1,1,3],4],
        ['?#?#?#?#?#?#?#?', [1,3,1,6],1],
        ['????.#...#...', [4,1,1],1],
        ['????.######..#####.', [1,6,5],4],
        ['?###????????', [3,2,1],10],
        ]
    for c in cases:
        assert solution.recurse(c[0],0,0,0,c[1], {}) == c[2]

def test_part_2_data():
    expected = ['???.###????.###????.###????.###????.###',[1,1,3,1,1,3,1,1,3,1,1,3,1,1,3,]]
    assert expected == solution.update_for_part_two(['???.###',[1,1,3]])
