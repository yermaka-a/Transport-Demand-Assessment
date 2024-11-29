import pandas as pd
from numpy import isnan
from global_variables import GLOBAL_VALUES_CONTAINER as values
from tk_root import tk
import os
from events.input_events import keyRelease_long_input
from Exceptions.notFoundXls import NotFoundXls
from Exceptions.notFoundInOutFolder import NotFoundInOutFolder
def split_symbols_and_digits(el):
     symbols = ""
     digits = ""
     for i in range(len(list(el))):
         if el[i] >= 'A'  and el[i].upper() <= 'Z':
            symbols += el[i].upper()
         elif el[i] >= '0'  and el[i] <= '9':
            digits += el[i]
     symbols = list(symbols)
     countOfSym = 0
     lenSymsMinusOne = len(symbols) - 1
     for i in range(len(symbols)):
        if i != lenSymsMinusOne:
            countOfSym += (26**(len(symbols) - (i+1)) * (ord(symbols[i]) - 64))
        elif i == lenSymsMinusOne:
            countOfSym += (ord(symbols[i]) - 65)
     symbols = countOfSym
     return (symbols, int(digits))
def get_data_from_xls():
    try:
        filename_in = values["filename_in_value"].get()
        if os.path.isdir("./Исходные данные"):
            if os.path.isfile(f"./Исходные данные/{filename_in}.xlsx"):
                path =f"./Исходные данные/{filename_in}.xlsx"
            elif os.path.isfile(f"./Исходные данные/{filename_in}.xls"):
                path = f"./Исходные данные/{filename_in}.xls"
            else:
                raise NotFoundXls(f"В папке 'Исходные данные'. Файл с именем {filename_in}  не найден! Его необходимо добавить.", 1)
        else:
            raise NotFoundInOutFolder(f"Папка с именем 'Исходные данные' не найдена, возможно её надо создать вручную в папке с программой!", 2)
        df = pd.read_excel(path, header=None)
        xls1_values = list(map(lambda el: split_symbols_and_digits(el), values["first_bounds_value"].get().split(" ")))
        xls2_values = list(map(lambda el: split_symbols_and_digits(el), values["second_bounds_value"].get().split(" ")))
        print(xls1_values , xls2_values)
        print(values["first_bounds_value"].get().split(" ") , values["second_bounds_value"].get().split(" "))
        arr1 = []
        arr2 = []
        print(xls1_values[0][1]-1, xls1_values[1][1], xls1_values[0][0], xls1_values[1][0]+1)
        for el in df.iloc[xls1_values[0][1]-1:xls1_values[1][1], xls1_values[0][0]:xls1_values[1][0]+1].itertuples(index=True):
            arr1.append(el[1])
        for el in df.iloc[xls2_values[0][1]-1:xls2_values[1][1], xls2_values[0][0]:xls2_values[1][0]+1].itertuples(index=True):
            arr2.append(el[1])
        print(arr1, arr2)
        values["long_input1"].set(value=" ".join(map(str, list(map(int, filter(lambda x: x>=0 and not isnan(x), arr1))))))
        values["long_input2"].set(value=" ".join(map(str, list(map(int, filter(lambda x: x>=0 and not isnan(x), arr2))))))
        keyRelease_long_input(0, "long_input1")
        keyRelease_long_input(1, "long_input2")
    except (NotFoundXls, NotFoundInOutFolder) as e:
         tk.messagebox.showwarning("Файл или папка не найдены!", f"{e}")
    except Exception as e:
        tk.messagebox.showwarning("Непредвиденная ошибка!", f"Вот что случилось: {e}")
