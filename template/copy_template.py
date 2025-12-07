import glob
import os
import sys

def challenge_count(year):
    if int(year) < 2025:
        return 25
    return 12

def main(year):
    interesting_files = ['solution.py','test_solution.py']
    existing = glob.glob(f'../{year}/*')
    for i in range(1, challenge_count(year) + 1):
        folder_name = f'../{year}/{i:>02}'
        if folder_name not in existing:
            os.system(f'mkdir {folder_name}')
            for f in interesting_files:
                execution = f'cp {f} {folder_name}/{f}'
                os.system(execution)

def get_year():
    vals = sys.argv
    if len(vals) != 2:
        raise ValueError(f"Expected single arugment, got {len(vals)}")
    if int(vals[1]) < 2015 or int(vals[1]) > 2026:
        raise ValueError(f"Argument needs to be a valid year")
    return vals[1]

if __name__ == "__main__":
    year = get_year()
    main(year)
