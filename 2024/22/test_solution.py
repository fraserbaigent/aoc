import solution
test_data = [int(l.strip()) for l in '''1
10
100
2024

'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 37327623
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 23
    assert solution.part_2([1,2,3,2024]) == expected_part_2

def test_prune():
    assert 16113920 == solution.prune(100000000)

def test_mix():
    assert 37 == solution.mix(42, 15)
