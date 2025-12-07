import solution
test_data = [tuple(l.split('-')) for l in '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''.split(',')]

def test_part_1():
    expected_part_1 = 1227775554
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 4174379265
    assert solution.part_2(test_data) == expected_part_2
    pass

def test_get_lb():
    assert solution.get_lower_bound("123","456") is None
    assert solution.get_lower_bound("1","16") == "10"
    assert solution.get_lower_bound("12345","123456") == "100000"
    assert solution.get_lower_bound("123456789","1234567891") == "1000000000"

def test_clean_data():
    test_data_2 = [
        ("99", "199"),
        ("12345", "123456"),
        ]
    expected = [("99", "99"),("100","199"),("12345","99999"),("100000","123456")]
    assert solution.clean_data(test_data_2) == expected

def test_cases_pt_2():
    assert solution.part_2([("11","22")]) == 33
    assert solution.part_2([("99","111")]) == 210
    assert solution.part_2([("998","1012")]) == 2009
    assert solution.part_2([("1188511880","1188511890")]) == 1188511885
    assert solution.part_2([("222220","222224")]) == 222222
