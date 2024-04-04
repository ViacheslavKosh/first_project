import sys
from pathlib import Path

def main(path):
    path = Path(path)
    for element in path.iterdir():
        if element.is_dir():
            print(f'Folder: {element}')
        else:
            print(f'File: {element}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Entered wrong number of arguments')
    else:
        path = sys.argv[1]
        main(path)