import solution
test_data = [l.strip() for l in '''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a                                
'''.split('\n') if len(l.strip())]

test_data_2 = [l.strip() for l in '''
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 32000000
    assert solution.part_1(test_data) == expected_part_1

def test_part_1_2():
    expected_part_1 = 11687500
    assert solution.part_1(test_data_2) == expected_part_1
    
def test_part_2():
    expected_part_2 = 0
    assert solution.part_2(test_data) == expected_part_2

def test_parse_data():
    expected = {
        'button':{
            'type': solution.BUTTON,
            'vals':['broadcaster'],
            },
        'broadcaster':{
            'type':solution.BROADCASTER,
            'vals':['a','b','c'],
                },
        'a' :{
            'type':solution.FLIP_FLOP,
            'vals':['b'],
            },
        'b' :{
            'type':solution.FLIP_FLOP,
            'vals':['c'],
            },
        'c' :{
            'type':solution.FLIP_FLOP,
            'vals':['inv'],
            },
        'inv': {
            'type':solution.CONJUNCTION,
            'vals' : ['a'],
            'inputs' :['c'],
            },
        }
    assert expected == solution.parse_data(test_data)
