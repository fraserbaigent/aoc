def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return infile.readlines()

data = get_data('data.dat')

################################################################################

import re

def parse_line(line):
    dat = re.compile('Game (\d+): (.*)')
    res = dat.match(line)
    game_id = int(res.groups()[0])

    colour_regex = re.compile('(\d+) (\w+)')
    games = list()
    g_str = res.groups()[1]
    for game in g_str.split(';'):
        game_result = dict()
        for batch in game.split(','):
            batch = batch.strip()
            res_2 = colour_regex.match(batch)
            game_result[res_2.groups()[1]]=int(res_2.groups()[0])
        games.append(game_result)
    return (game_id, games)

def is_possible(game_list, configuration):
    for g in game_list:
        for c in g:
            if c not in configuration or g[c] > configuration[c]:
                return False
    return True
    
def part_1():
    total = 0
    configuration = {'red':12,'green':13,'blue':14}
    for l in data:
        l = l.strip()
        
        game_id, games = parse_line(l)
        if is_possible(games, configuration):
            total += game_id
    print(f'Part 1: {total}')

def get_minimum_cubes(games):
    minimums = dict()
    for g in games:
        for c in g:
            if c not in minimums or minimums[c]<g[c]:
                minimums[c]=g[c]

    return minimums

def part_2():
    total = 0
    configuration = {'red':12,'green':13,'blue':14}
    for l in data:
        l = l.strip()
        
        game_id, games = parse_line(l)
        mins = get_minimum_cubes(games)
        v = 1
        for v_i in mins.values():
            v*=v_i
        total+=v
    print(f'Part 2: {total}')
    
part_1()
part_2()
