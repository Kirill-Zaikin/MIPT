import os #обращение к операционной и файловой системам
import time #модуль времени
import psutil #данные программы
from datetime import datetime #обращение к дате
from tqdm import tqdm #прогресс бар

program_name = os.path.basename(__file__)

def clear_terminal():

    # Для Windows
    if os.name == 'nt':

        os.system('cls')
    # Для Unix/Linux/Mac
    else:

        os.system('clear')

clear_terminal()

size = os.get_terminal_size()
width = size.columns
height = size.lines

text_start = f'ЗАПУСК ПРОГРАММЫ: {program_name}'
len_start = len(text_start)
len_output = '-' * (width)
text_start_output =  f'{text_start}\n{len_output}\n\n'

text_stop = f'ЗАВЕРШЕНИЕ ПРОГРАММЫ: {program_name}'
len_stop = len(text_stop)
text_stop_output =  f'\n{len_output}\n{text_stop}\n'

class Console:

    def __init__(self, text, time_stop = 0.05) -> str:

        self.text = str(text)
        self.time_stop = time_stop
        time.sleep(1)

        for char in self.text:

            print(char, end='', flush=True)
            time.sleep(time_stop)

        print()

class Summary(Console):

    def __init__(self, time_start, time_stop, date):
        
        self.start = time_start
        self.stop = time_stop
        self.date = date

        self.time_work = self.stop - self.start

        Console('СВОДКА РАБОТЫ ПРОГРАММЫ:\n',0.015)
        Console(f' - Время работы программы: {self.time_work:.4f} сек.', 0.015)
        Console(f' - Объём памяти: {psutil.Process().memory_info().rss / 1024 ** 2:.4f} МБ (учитывая оболочку сводки работы программы)', 0.015)

        Console(f'\nДата формирования сводки для "{program_name}": {self.date}\n', 0.015)

Console(f'ЗАГРУЗКА ТЕРМИНАЛА')
for i in tqdm(range(20)):
    time.sleep(0.1)
Console(f'ТЕРМИНАЛ ЗАГРУЖЕН')

Console(f'\n{text_start_output}', 0.015)

programm_time_start = time.time()

#НАЧАЛО ПОЛЬЗОВАТЕЛЬСКОГО КОДА
#---------------------------------------------------------------------------------------------------------------------------------------------------

def console_text(text_output, time_output):
    return Console(text_output, time_output)

#---------------------------------------------------------------------------------------------------------------------------------------------------
#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

programm_time_stop = time.time()

Console(text_stop_output, 0.015)

Summary(programm_time_start, programm_time_stop, datetime.now())