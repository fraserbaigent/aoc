from AocCommon import get_data, data_to_list_grid


data = get_data()
data= data_to_list_grid(data)

##########################################################################
DIRS = [(0,1),(1,0),(0,-1),(-1,0)]

def visit(coord, grid, visited):
    x,y=coord
    visited.add(coord)

    area = 1
    perimeter = 0
    for dx,dy in DIRS:
        x_i = x+dx
        y_i = y+dy
        if y_i < 0 or x_i < 0 or y_i >= len(grid) or x_i >= len(grid[0]):
            perimeter += 1
            continue
        if grid[y][x] == grid[y_i][x_i]:
            if (x_i,y_i) in visited:
                continue
            a, p = visit((x_i,y_i), grid, visited)
            area += a
            perimeter += p
        else:
            perimeter += 1
    return area, perimeter

def visit_2(coord, grid, visited):
    x,y=coord
    visited.add(coord)

    area = 1
    perimeter = [0 for d in DIRS]
    corners = 0
    for i,(dx,dy) in enumerate(DIRS):
        x_i = x+dx
        y_i = y+dy
        if y_i < 0 or x_i < 0 or y_i >= len(grid) or x_i >= len(grid[0]):
            perimeter[i]=1
            continue
        if grid[y][x] == grid[y_i][x_i]:
            if (x_i,y_i) not in visited:
                a, c = visit_2((x_i,y_i), grid, visited)
                area += a
                corners += c
        else:
            perimeter[i] = 1

        dx2, dy2 = DIRS[(i+1)%len(DIRS)]
        x2 = x + dx2
        y2 = y + dy2
        if x2>=0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid):
            if grid[y][x] == grid[y_i][x_i] and grid[y2][x2] == grid[y][x]:
                xx = x_i if x == x2 else x2
                yy = y_i if y == y2 else y2
                if x == 2 and y == 1:
                    print(x,y,xx,yy)
                
                if grid[yy][xx] != grid[y][x]:
                    corners+=1
        
    for i in range(0, len(perimeter)):
        if perimeter[i] == 1 and perimeter[(i-1)%len(perimeter)] == 1:
            corners += 1
            
    return area, corners


def solve_part_1(data):
    total=0
    visited = set()
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            if (x,y) not in visited:
                a,p= visit((x,y), data, visited)
                total += a*p
    return total

def solve_part_2(data):
    total=0
    visited = set()
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            if (x,y) not in visited:
                a,sides= visit_2((x,y), data, visited)
                print('tot',a,sides)
                total += a*sides
    return total

def part_1(data):
    total = solve_part_1(data)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = solve_part_2(data)
    
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
