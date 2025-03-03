import sys
from pathlib import Path
from colorama import Fore


directory = Path(sys.argv[1])


def print_files(directory: Path, indent: int = 0):

    if not directory.exists():
        print(Fore.RED + f"Error: path '{directory}' no exists.")
        return
    if not directory.is_dir():
        print(Fore.RED + f"Error: path '{directory}' not directory.")
        return
    
    for path in sorted(directory.iterdir()):
        prefix = " " * indent
        if path.is_dir():
            print(Fore.BLUE + f"{prefix}{path.name}/")

            print_files(path, indent + 2)
        else:
            print(Fore.YELLOW + f"{prefix}{path.name}")
            

print_files(directory)

