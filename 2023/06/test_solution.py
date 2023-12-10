import solution
test_data = [l.strip() for l in '''
Time:      7  15   30
Distance:  9  40  200
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 288
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 71503
    assert solution.part_2(test_data) == expected_part_2

def test_distance_calculation():
    races = [
        [7,9,2,5],
        [15,40,4,11],
        [30,200,11,19],
        ]

    for r in races:
        assert (r[2],r[3]) == solution.distance_calculation(r[0],r[1],1)
        
        
