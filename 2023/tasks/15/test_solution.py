import solution

test_data = [
    l.strip()
    for l in """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".split(
        "\n"
    )
    if len(l.strip())
]


def test_hash():
    assert solution.hash_string("HASH") == 52
    assert solution.hash_string('npq') == 255
    assert solution.hash_string('qkc') == 255

def test_part_1():
    expected_part_1 = 1320
    assert solution.part_1(test_data) == expected_part_1


def test_part_2():
    expected_part_2 = 145
    assert solution.part_2(test_data) == expected_part_2
