import json
import solution
test_data = [l.strip() for l in '''
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 0
 #   assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 0
#    assert solution.part_2(test_data) == expected_part_2

def test_get_robot_routes():
    test_code = "^A>AA"
    mapping = solution.get_pad_map("X^A\n<v>")
    shortest_arrow_map = solution.get_shortest_route_map(mapping)    
    test_robot = ('A', shortest_arrow_map)
    expected_routes = ['<A>AvA^AA']
    assert expected_routes == solution.get_robot_routes(test_code, test_robot)
    
def test_get_robot_routes_2():
    test_code = "^"
    mapping = solution.get_pad_map("X^A\n<v>")
    shortest_arrow_map = solution.get_shortest_route_map(mapping)    
    test_robot = ('A', shortest_arrow_map)
    expected_routes = ['<A']
    assert expected_routes == solution.get_robot_routes(test_code, test_robot)


def test_get_robot_routes_3():
    test_code = "<>A^"
    mapping = solution.get_pad_map("X^A\n<v>")
    shortest_arrow_map = solution.get_shortest_route_map(mapping)    
    test_robot = ('A', shortest_arrow_map)
    expected_routes = ['<<vA>>A^A<A', '<v<A>>A^A<A', 'v<<A>>A^A<A']
    assert sorted(expected_routes) == sorted(solution.get_robot_routes(test_code, test_robot))
    print(json.dumps(shortest_arrow_map,indent=4))
    assert False
        
