import solution
test_data = [l.strip() for l in '''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9                                
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 5
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 7
    assert solution.part_2(test_data) == expected_part_2

def test_intersects():

    assert solution.intersects(0,2,1,1) == True
    assert solution.intersects(0,0,0,2) == True
    assert solution.intersects(4,4,0,0) == False
    
def test_2():
    test_data = [l.strip() for l in '''
0,0,1~0,0,1
0,0,2~4,0,2
0,0,3~0,0,3
4,0,4~4,4,4
0,0,10~4,0,10
0,0,12~4,0,12                                    
'''.split('\n') if len(l.strip())]
    assert solution.part_2(test_data) == 6
