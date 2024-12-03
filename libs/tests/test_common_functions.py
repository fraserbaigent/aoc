import AocCommon

def test_split_data_with_regex():
    test_data = [
        '123 abc 987|abc',
        '456 def 838|zzz',
        ]
    expected = [
        ['123','abc','987','abc'],
        ['456','def', '838','zzz'],
        ]
    test_pattern = '(\\d+) (\\w+) (\\d+)\\|(\\w+)'
    assert AocCommon.split_data_with_regex(test_data, test_pattern) == expected


def test_split_data_with_regex_ignore():
    test_data = [
        '123 abc 987|abc',
        'failure',        
        '456 def 838|zzz',
        ]
    expected = [
        ['123','abc','987','abc'],
        ['456','def', '838','zzz'],
        ]
    test_pattern = '(\\d+) (\\w+) (\\d+)\\|(\\w+)'
    assert AocCommon.split_data_with_regex(test_data, test_pattern, filter_failures = True) == expected

def test_split_data_with_regex_cast():
    test_data = [
        '123 abc 987|abc',
        '456 def 838|zzz',
        ]
    expected = [
        [123,'abc','987','abc'],
        [456,'def', '838','zzz'],
        ]
    test_pattern = '(\\d+) (\\w+) (\\d+)\\|(\\w+)'
    assert AocCommon.split_data_with_regex(test_data, test_pattern, filter_failures = True,
                                           types = [int, str, str, str]) == expected
    
