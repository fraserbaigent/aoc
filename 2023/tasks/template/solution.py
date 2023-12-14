import sys
import requests
import os
import re

def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]

def to_submit():       
    if len(sys.argv) == 1:
        return False, False
    elif len(sys.argv) > 2:
        print(f'Too many arguments')
        sys.exit(1)
    return "s1" in sys.argv, "s2" in sys.argv

def get_cookie() -> str:
    with open ('../../.cookie_secret','r') as infile:
        return infile.read()

def get_date_data():
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    regex = re.compile('^.*/(\\d{4})/(\\d{2})$')
    res = regex.match(current_file_directory)
    return res.groups()[0], res.groups()[1]
    
def submit(answer, question):
    year, day = get_date_data()
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    session_cookie = get_cookie()    
    headers = {
        "User-Agent": "YourCustomUserAgentHere",
        "Cookie": f"session={session_cookie}",
    }
    payload = f"level={question}&answer={answer}"

    response = requests.post(url, data=payload, headers=headers)
    print(f'Response: {response.status_code}: \n', response.text)
    
data = get_data("data.dat")

##########################################################################


def solve_part_1(data):
    pass

def solve_part_2(data):
    pass

def part_1(data, to_submit):
    total = solve_part_1(data)
    print(f"Part 1: {total}")
    if to_submit == True:
        submit(total, 1)
    return total


def part_2(data, to_submit):
    total = solve_part_2(data)
    
    print(f"Part 2: {total}")
    if to_submit == True:
        submit(total, 1)    
    return total


if __name__ == "__main__":
    submit_1, submit_2 = to_submit()
    part_1(data, submit_1)
    part_2(data, submit_2)
