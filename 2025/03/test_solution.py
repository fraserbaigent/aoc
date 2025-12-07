import solution
test_data = [l.strip() for l in '''987654321111111
811111111111119
234234234234278
818181911112111
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 357
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 3121910778619
    assert solution.part_2(test_data) == expected_part_2

def test_part_2_2():
    test_data_2 = [
        "3122332423322225345222222534622225632332132222223344225223521231422631222311222322214431252352422412",        
        ]
    assert 666552422412 == solution.part_2(test_data_2) 
    
