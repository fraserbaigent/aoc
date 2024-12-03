import re
import requests
import sys
import os

def get_cookie(cookie_secret_path : str) -> str:
    with open (cookie_secret_path,"r") as infile:
        return infile.read()

def get_data() -> list:
    with open("data.dat", "r") as infile:
        return [l.strip() for l in infile.readlines() if l.strip() != ""]

def get_data_blob() -> str:
    with open("data.dat", "r") as infile:
        return infile.read()

def data_to_list_grid(data : list,
                      separator : str = None,
                      ty = None) -> list:
    grid = []
    for d in data:
        if separator is None:
            grid.append([d_i for d_i in d])
        else:
            grid.append(d.split(separator))
        if ty is not None:
            for i in range(len(grid[-1])):
                grid[-1][i] = ty(grid[-1][i])
    return grid

def split_data_with_regex(data : list,
                          pattern : str,
                          filter_failures : bool = False,
                          types : list = None) -> list:
    grid = []
    regex = re.compile(pattern)
    for d in data:
        res = regex.match(d)
        if not filter_failures or res is not None:
            if types is None:
                grid.append(list(res.groups()))
            else:
                grid.append([t(v) for t, v in zip(types, res.groups())])
    return grid   
    
def should_submit_task() -> tuple:
    if len(sys.argv) == 1:
        return False, False
    elif len(sys.argv) > 2:
        print(f"Too many arguments provided: {sys.argv}")
        sys.exit(1)
    return "s1" in sys.argv, "s2" in sys.argv

def get_date_data():
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    regex = re.compile("^.*/(\\d{4})/(\\d{2})$")
    res = regex.match(current_file_directory)
    return res.groups()[0], res.groups()[1]
    
def submit(answer : str,
           question : str):
    year, day = get_date_data()
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    session_cookie = get_cookie()    
    headers = {
        "User-Agent": f"aoc agent {year}",
        "Cookie": f"session={session_cookie}",
    }
    payload = f"level={question}&answer={answer}"

    response = requests.post(url, data=payload, headers=headers)
    print(f"Response: {response.status_code}: \n", response.text)
    
    
