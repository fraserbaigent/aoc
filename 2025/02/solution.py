from AocCommon import get_data, get_data_blob, data_to_list_grid, split_data_with_regex

def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [tuple(l.split('-')) for l in infile.readlines()[0].strip().split(",")]


data = get_data("data.dat")
#data = get_data_blob()
#data = data_to_list_grid()
#data = split_data_with_regex(data, "add pattern")

##########################################################################

def get_lower_bound(lbound, ubound):
    lower = lbound
    
    if len(lbound) %2 != 0:
        if len(lbound) == len(ubound):
            return None
        lower = f'1{"0" * int((len(ubound) -1))}'
        
    return lower
    

def solve_part_1(data):
    total = 0
    for lbound, ubound in data:
        lstr = get_lower_bound(lbound,ubound)
        if lstr is None:
            continue
        lowest_val = int(lstr[:int(len(lstr)/2)])
        while True:
            cv = int(f'{lowest_val}{lowest_val}')
            if cv > int(ubound):
                break
            elif cv >= int(lbound):
                total += cv
            lowest_val += 1
    return total

def clean_data(data):
    cleaned = []
    for lb, ub in data:
        if len(lb) == len(ub):
            cleaned.append((lb,ub))
        else:
            nxt = f'1{"0" * int((len(ub) -1))}'
            cleaned.append((lb, str(int(nxt)-1)))
            cleaned.append((nxt, ub))
        
    return cleaned

def solve_part_2(data):
    total = 0
    data = clean_data(data)
    for lbound, ubound in data:
       lstr = lbound
       seen_vals = set()
       for r in range(1, len(ubound)):
           ss = int(lbound[:r])
           if len(ubound) % r != 0:
               continue
           
           m = len(ubound) // r
           while True:
               v = int(str(ss) * m)
               if v > int(ubound):
                   break
               elif v >= int(lbound):
                   if v not in seen_vals:
                       total += v
                       seen_vals.add(v)
               ss += 1

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
