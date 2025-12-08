import solution
test_data = [l for l in '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 4277556
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 3263827
    assert solution.part_2(test_data) == expected_part_2
