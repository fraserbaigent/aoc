import solution

def test_parse_line():
    line = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'


    result = solution.parse_line(line)
    expected = (1, [{'blue':3,'red':4},{'red':1,'green':2,'blue':6},{'green':2}])
        
    assert expected==result

