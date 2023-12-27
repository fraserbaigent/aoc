import solution
test_data = [l.strip() for l in '''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr

'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 0
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 0
    assert solution.part_2(test_data) == expected_part_2
