import xlsxwriter
from openpyxl import load_workbook
import pandas as pd
from global_variables import GLOBAL_VALUES_CONTAINER as values, GLOBAL_INPUTS_CONTAINER as inputs
from tk_root import tk
from modelsTree.events.input_events import keyRelease_long_input
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
    path = values["path_input"].get()
    print("path: ", path)
    df = pd.read_excel(path, header=None)
    xls1_values = list(map(lambda el: split_symbols_and_digits(el), values["xls_input1"].get().split(" ")))
    xls2_values = list(map(lambda el: split_symbols_and_digits(el), values["xls_input2"].get().split(" ")))
    print("xls1_values: ", xls1_values, "\n xls2_values: ", xls2_values)
    # for i in range(xls1_values)
    arr1 = []
    arr2 = []
    for el in df.iloc[xls1_values[0][1]-1:xls1_values[1][1], xls1_values[0][0]:xls1_values[1][0]+1].itertuples(index=True):
        arr1.append(el[1])
    for el in df.iloc[xls2_values[0][1]-1:xls2_values[1][1], xls2_values[0][0]:xls2_values[1][0]+1].itertuples(index=True):
        arr2.append(el[1])
    inputs["long_input1"].delete(0, tk.END)
    inputs["long_input1"].insert(0," ".join(map(str, arr1)))
    inputs["long_input2"].delete(0, tk.END)
    inputs["long_input2"].insert(0," ".join(map(str, arr2)))
    keyRelease_long_input(0, "long_input1")
    keyRelease_long_input(1, "long_input2")
