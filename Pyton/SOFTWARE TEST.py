import os
import time

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len = 200
print("-" * max_len)

class Console:
    def __init__(self, text) -> str:
        self.text = str(text)
        time.sleep(1)
        for char in self.text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()

#НАЧАЛО ПОЛЬЗОВАТЕЛЬСКОГО КОДА



#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

print("-" * max_len)