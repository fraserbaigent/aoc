import solution
test_data = [l.strip() for l in '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''.split()]

def test_part_1():
    total = 0
    for row in range(0,len(test_data)):
        line = test_data[row]
        for column in range(0, len(line)):
            if line[column] not in solution.ignore:
                total += solution.find_part_number(column, row, test_data)
    assert total==4361
