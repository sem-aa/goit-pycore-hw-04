from pathlib import Path

from typing import Tuple

def total_salary(path: str) -> Tuple[int, float]:
    try:
        with open(Path(path) , 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return (0, 0)
            
            # use generator to extract and sum salaries
            total = sum(int(line.split(",")[1]) for line in lines)
            average = float(total / len(lines)) 
            return (total, average)
        
    except FileNotFoundError:
        print("File not found")
    
    except Exception as e:
        print(f"Error: {e}")  
         
    
total, average = total_salary("./employees.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")