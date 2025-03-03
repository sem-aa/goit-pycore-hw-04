from pathlib import Path
from typing import List, Dict

def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_info = []
    try:
        with open(Path(path) , 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return cats_info
            
            for line in lines:
                id, name, age = line.strip().split(",")
                cats_info.append({
                    "id": id, "name": name, "age": age
                })

            return cats_info
    except FileNotFoundError:
        print("File not found")
        return cats_info
    except Exception as e:
        print(f"Error: {e}")   
        return cats_info 


cats_info = get_cats_info("./cats.txt")
print(cats_info)

