import xlsxwriter
from openpyxl import load_workbook
# Add a sheet to the workbook

def write_to_xls_gravit_model(book, num_of_iterations, k, kolvo_iter, X1, X2, X3,SumStr, SumStb, K, K1, Eiter, Er, n):
      if len(num_of_iterations) == 1:
            if k <= num_of_iterations[0]:
                try:
                     sheet1 = book.add_worksheet(f"{kolvo_iter}")
                except xlsxwriter.exceptions.DuplicateWorksheetName:
                     sheet1 = book.get_worksheet_by_name(f"{kolvo_iter}")
                sheet1.write(0, 1, f"Итерация №-{kolvo_iter}")
                sheet1.write(3, 0, "X1")
                for i in range(len(X1)):
                    for j in range(len(X1)):
                        sheet1.write(i+4, j, X1[i][j])
                sheet1.write(len(X1)+5, 0, "SumStb")
                for i in range(len(SumStb)):
                    sheet1.write(len(X1)+6, i, SumStb[i])
                sheet1.write(len(X1)+8, 0, "K")
                for i in range(len(K)):
                    sheet1.write(len(X1)+9, i, K[i])
                sheet1.write(len(X1)+10, 0, "X2")
                for i in range(n-1):
                    for j  in range(i+1, n):
                        sheet1.write(len(X1)+11+i, j, X2[i][j])
                sheet1.write(len(X1)+12+len(X2), 0, "Er")
                sheet1.write(len(X1)+12+len(X2), 3, "MaxEr: ")
                sheet1.write(len(X1)+12+len(X2), 4, Eiter)
                for i in range(n-1):
                    for j  in range(i+1, n):
                        sheet1.write(len(X1)+len(X2)+13+i, j, Er[i][j])
                sheet1.write(len(X1)+len(X2)+15+len(Er), 0, "SumStr")
                for i in range(len(SumStr)):
                    sheet1.write(len(X1)+len(X2)+16+len(Er), i, SumStr[i])
                sheet1.write(len(X1)+len(X2)+18+len(Er), 0, "K1")
                for i in range(len(K1)):
                    sheet1.write(len(X1)+len(X2)+19+len(Er), i, K1[i])
                sheet1.write(len(X1)+len(X2)+20+len(Er), 0, "X3")
                for i in range(n-1):
                    for j  in range(i+1, n):
                        sheet1.write(len(X1)+len(X2)+21+i+len(Er), j, X3[i][j])
      elif len(num_of_iterations) == 2:
            if k >= num_of_iterations[0] and k <= num_of_iterations[1]:
                try:
                     sheet1 = book.add_worksheet(f"{kolvo_iter}")
                except xlsxwriter.exceptions.DuplicateWorksheetName:
                     sheet1 = book.get_worksheet_by_name(f"{kolvo_iter}")
                sheet1.write(0, 1, f"Итерация №-{kolvo_iter}")
                sheet1.write(3, 0, "X1")
                for i in range(len(X1)):
                    for j in range(len(X1)):
                        sheet1.write(i+4, j, X1[i][j])
                sheet1.write(len(X1)+5, 0, "SumStb")
                for i in range(len(SumStb)):
                    sheet1.write(len(X1)+6, i, SumStb[i])
                sheet1.write(len(X1)+8, 0, "K")
                for i in range(len(K)):
                    sheet1.write(len(X1)+9, i, K[i])
                sheet1.write(len(X1)+10, 0, "X2")
                for i in range(n-1):
                    for j  in range(i+1, n):
                        sheet1.write(len(X1)+11+i, j, X2[i][j])
                sheet1.write(len(X1)+12+len(X2), 0, "Er")
                sheet1.write(len(X1)+12+len(X2), 3, "MaxEr: ")
                sheet1.write(len(X1)+12+len(X2), 4, Eiter)
                for i in range(n-1):
                    for j  in range(i+1, n):
                        sheet1.write(len(X1)+len(X2)+13+i, j, Er[i][j])
                sheet1.write(len(X1)+len(X2)+15+len(Er), 0, "SumStr")
                for i in range(len(SumStr)):
                    sheet1.write(len(X1)+len(X2)+16+len(Er), i, SumStr[i])
                sheet1.write(len(X1)+len(X2)+18+len(Er), 0, "K1")
                for i in range(len(K1)):
                    sheet1.write(len(X1)+len(X2)+19+len(Er), i, K1[i])
                sheet1.write(len(X1)+len(X2)+20+len(Er), 0, "X3")
                for i in range(n-1):
                    for j  in range(i+1, n):
                        sheet1.write(len(X1)+len(X2)+21+i+len(Er), j, X3[i][j])

# Формирование сумм ai*bj по строкам
def write_to_xls_S1(book,  S1, n):
    try:
        sheet1 = book.add_worksheet("1")
    except xlsxwriter.exceptions.DuplicateWorksheetName:
        sheet1 = book.get_worksheet_by_name("1")
    sheet1.write(0, 0, "S1")
    sheet1.write(0, 3, "Формирование сумм ai*bj по строкам")
    for i in range(n):
        sheet1.write(1, i, S1[i])

def write_to_xls_robast_model(book, X):
    try:
        sheet1 = book.add_worksheet("Робастная модель")
    except xlsxwriter.exceptions.DuplicateWorksheetName:
        sheet1 = book.get_worksheet_by_name("Робастная модель")
    sheet1.write(0, 0, "Робастная модель")
    for i in range(len(X)):
        for j in range(len(X[i])):
            sheet1.write(i+2, j, X[i][j])
    book.close()
