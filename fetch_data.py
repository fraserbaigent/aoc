import requests
import sys
from AocCommon import get_cookie

def get_args():    
    if len(sys.argv) != 3:
        print("Usage: python fetch_data.py <year> <day>")
        sys.exit(1)

    try:
        return int(sys.argv[1]),int(sys.argv[2])
    except:
        print(f'Year and day must be integer numbers')
        sys.exit(1)
    
def get_task(year, day, headers):
    url = f"https://adventofcode.com/{year}/day/{day}"    
    response = requests.get(url, headers=headers)
    return response.text
    
def get_input(year, day, headers):
    url = f"https://adventofcode.com/{year}/day/{day}/input"    
    response = requests.get(url, headers=headers)
    return response.text

def write_task(task, year, day):
    with open(f'{year}/{day:>02}/task.html','w') as task_file:
        task_file.write(task)

def write_data(data, year, day):
    with open(f'{year}/{day:>02}/data.dat','w') as data_file:
        data_file.write(data)
   
def get_challenge():    
    session_cookie = get_cookie('.cookie_secret')
    year, day = get_args()
        
    headers = {
        "User-Agent": "YourCustomUserAgentHere",
        "Cookie": f"session={session_cookie}",
    }

    task = get_task(year, day, headers)
    data = get_input(year, day, headers)

    write_task(task, year, day)
    write_data(data, year, day)
    
if __name__ == "__main__":
    get_challenge()
