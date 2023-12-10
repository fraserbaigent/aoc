import glob
import os


def main():
    interesting_files = ['task.dat','solution.py','data.dat','test_solution.py']
    existing = glob.glob('../*')
    for i in range(1,26):
        folder_name = f'../{i:>02}'
        if folder_name not in existing:
            os.system(f'mkdir {folder_name}')
            for f in interesting_files:
                execution = f'cp {f} {folder_name}/{f}'
                os.system(execution)
            
if __name__ == "__main__":
    main()
