import requests

def get_cookie() -> str:
    with open ('.cookie_secret','r') as infile:
        return infile.read()
    
def get_task(year, day, headers):
    url = f"https://adventofcode.com/{year}/day/{day}"    
    response = requests.get(url, headers=headers)
    return response.text
    
def get_input(year, day, headers):
    url = f"https://adventofcode.com/{year}/day/{day}/input"    
    response = requests.get(url, headers=headers)
    return response.text

def write_task(task, day):
    with open(f'{day:<02}/task.dat','w') as task_file:
        task_file.write(task)

def write_data(task, day):
    with open(f'{day:<02}/data.dat','w') as data_file:
        data_file.write(data)
    
def get_challenge():    
    session_cookie = get_cookie()
    year = 2023
    day = 1
    
    headers = {
        "User-Agent": "YourCustomUserAgentHere",
        "Cookie": f"session={session_cookie}",
    }

    task = get_task(year, day, headers)
    data = get_input(year, day, headers)

    write_task(task, day)
    write_data(data, day)
    
