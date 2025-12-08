from AocCommon import data_to_list_grid, get_data, get_data_blob, split_data_with_regex

import solution
test_data = [l.strip() for l in '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689

'''.split('\n') if len(l.strip())]
test_data = data_to_list_grid(test_data, ",", int)

def test_part_1():
    expected_part_1 = 40
    assert solution.part_1(test_data, 10) == expected_part_1

def test_part_2():
    expected_part_2 = 0
#    assert solution.part_2(test_data) == expected_part_2
