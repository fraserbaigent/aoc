def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]

data = get_data('data.dat')

################################################################################
ignore = '0123456789.'
    
def find_number_in_row(row_string, part_index):
    parts=list()
    left_start_index = part_index-1
    try_2=True
    if not row_string[left_start_index].isnumeric():
        left_start_index+=1
        
    if row_string[left_start_index].isnumeric():
        while True:
            if left_start_index-1 >= 0 and row_string[left_start_index-1].isnumeric():
                left_start_index -= 1
            else:
                break
        end_index = part_index-1
        while True:
            if end_index+1 < len(row_string) and row_string[end_index+1].isnumeric():
                end_index += 1
                try_2=False
            else:
                end_index+=1
                break
        parts.append(int(row_string[left_start_index:end_index]))


    if try_2 and part_index+1<len(row_string) and row_string[part_index+1].isnumeric():
        end_index=part_index+1
        while True:
            if end_index+1 < len(row_string) and row_string[end_index+1].isnumeric():
                end_index += 1
            else:
                end_index+=1
                break
        parts.append(int(row_string[part_index+1:end_index]))
    return parts
    
def find_part_number(part_x, part_y, grid):
    parts = list()
    if part_y >0:
        to_add= find_number_in_row(grid[part_y-1], part_x)
        parts+=to_add
    to_add=find_number_in_row(grid[part_y], part_x)
    parts+=to_add
    if part_y < len(grid)-1:
        to_add=find_number_in_row(grid[part_y+1], part_x)
        parts+=to_add

    return parts

def part_1():
    total = 0
    for row in range(0,len(data)):
        line = data[row]
        for column in range(0, len(line)):
            if line[column] not in ignore:
                parts = find_part_number(column, row, data)
                total += sum(parts)
    print(f'Part 1: {total}')
    
def part_2():
    total = 0
    GEAR='*'
    for row in range(0,len(data)):
        line = data[row]
        for column in range(0, len(line)):
            if line[column] not in ignore:
                parts = find_part_number(column, row, data)
                if line[column] == GEAR and len(parts)==2:
                    total += parts[0]*parts[1]
    print(f'Part 2: {total}')

part_1()
part_2()
