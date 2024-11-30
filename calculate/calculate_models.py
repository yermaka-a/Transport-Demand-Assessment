import numpy as np
import xlsxwriter
import  xls.write_to_xls as wtxls
from global_variables import GLOBAL_VALUES_CONTAINER as values, GLOBAL_PLOTSDATA as plots_data
import os
from tk_root import tk
def calculate_models(is_write, is_plot):
    try:
        # Получение данных из инпутов
        long_input1 = values["long_input1"].get()
        long_input2 = values["long_input2"].get()
        count_of_iter_start = values["count_of_iter_start"].get()
        count_of_iter_end = values["count_of_iter_end"].get()
        if is_write:
            path = "./Вывод данных/"
            if values["autonum_files_value"].get():
                if not os.path.isdir(path):
                    os.mkdir("./Вывод данных/")
                count_files = len(os.listdir(path))
                filename_out = values["filename_out_value"].get()
                filename_input = f"{count_files + 1}_{filename_out}"
            else:
                filename_input = values["filename_out_value"].get()
            book = xlsxwriter.Workbook(f"./Вывод данных/{filename_input}.xlsx")
        # Здесь можно добавить обработку данных
        num_of_iterations = [int(count_of_iter_start) - 1, int(count_of_iter_end) - 1]
        print("num_of_iterations: ", num_of_iterations)
        aV = list(map(float, long_input1.strip().split(' ')))
        bV = list(map(float, long_input2.strip().split(' ')))
        # plot_graph(canvas, aV, bV)
        A = np.array(aV)
        B = np.array(bV)
        E = float(values["accuracy_value"].get())
        n = len(aV)
        X1 = np.zeros((n,n))
        X2 = np.zeros((n,n))
        X3 = np.zeros((n,n))
        # Итерация первая
        # Формирование сумм ai*bj по строкам
        S1 = [0 for i in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                S1[i]=S1[i]+aV[i]*bV[j]
                # print(f"A{i}B{j}",aV[i],bV[j])
        if is_write:
            wtxls.write_to_xls_S1(book, S1, n)
        # Матрица корреспонденции после первой итерации X1ij
        for i in range(n-1):
            for j in range(i+1, n):
                X1[i][j] = aV[i]*bV[j] / S1[i]*aV[i]
        # Итеративные приближения матрицы корреспонденций по достижении заданной
        # точности или истечении максимального числа итераций
        MaxIter = int(values["count_of_iter"].get())
        kolvo_iter = 0
        SumStb = [0 for i in range(n)]
        SumStr = [0 for i in range(n)]
        K = [0 for i in range(n)]
        K1 = [0 for i in range(n-1)]
        plots_data["errors"] = []
        for k in range(MaxIter):
            l = MaxIter
            #Итерация вторая - Балансировка по выходам (столбцам)
            #суммы по столбцам
            for j in range(1, n):
                for i in range(j):
                    SumStb[j] = SumStb[j]+X1[i][j]
            # print(f"SummStb: {k}", SumStb)
            # Поправочный коэффициент
            for j in range(1, n):
                K[j]=bV[j]/SumStb[j]
            # Балансировка по выходам
            for i in range(n-1):
                for j  in range(i+1, n):
                    X2[i][j]=K[j]*X1[i][j]
            Er = abs(X1 - X2)

            # невязки по каждому элементу
            # максимальная невязка
            Eiter = Er.max()
            if Eiter <= E:
                break
            kolvo_iter += 1
            l=j
            # Итерация третья - Балансировка по входам (строкам)
            # суммы по строкам
            for i in range(n-1):
                SumStr[i]=0
                for j in range(i+1, n):
                    SumStr[i] = SumStr[i]+X2[i,j]
                # Поправочный коэффициент
            for i in range(n-1):
                K1[i]=aV[i] / SumStr[i]
                # Балансировка по входам
            for i in range(n-1):
                for j in range(i+1,n):
                    X3[i][j] = K1[i]*X2[i][j]
            # загрузка в excel
            if is_write:
                wtxls.write_to_xls_gravit_model(book, num_of_iterations, k, kolvo_iter, X1, X2,X3,SumStr,SumStb, K, K1,Eiter, Er, n)
            if is_plot:
                plots_data["errors"].append(Er.max())
            SumStb = [0 for i in range(n)]
            SumStr = [0 for i in range(n)]
            K = [0 for i in range(n)]
            K1 = [0 for i in range(n)]
            # Вводим следующее приближение
            X1 = X3
        X = X1.round()
        # % Конец цикла итеративного приближения матрицы корреспонденций по достижении заданной
        # % точности или истечении максимального числа итераций гравитационным
        # % методом
        # % Разворачиваем полученную матрицу корреспонденций X1 в вектор столбец X01
        if is_plot:
            plots_data["corr_matrix"] = np.copy(X)
        X01 = []
        for i in range(n-1):
            for j in range(i+1, n):
                X01.append(X1[i][j])
        X02 = []
        X03 = []
        X02 = aV - np.sum(X1, axis=1)
        X03 = bV - np.sum(X1, axis=0)

        H1 = np.zeros((n-1,1))
        G1 = np.zeros((n-1,1))
        H2 = np.zeros((n-1,1))
        G2 = np.zeros((n-1,1))
        for i in range(n-1):
            if X02[i]>0:
                H1[i] = X02[i]
            else:
                G1[i] = X02[i]
            if X03[i+1]>0:
                H2[i] = X03[i+1]
            else:
                G2[i] = X03[i+1]
        X0 = np.concatenate((np.array(X01), np.array(H1), np.array(H2), np.array(G1), np.array(G2)), axis=None)

        lb = np.full((round(((n*n+7*n)/2-4))),0)
        # % Формируем ограничения на верхние границы переменных
        # ux ug uh - прилетает как параметр функции
        ux = np.max(aV+bV)
        ug = np.max(aV+bV)
        uh = np.max(aV+bV)
        Ubx = np.full(round(((n*n-n)/2)), ux)
        Ubg = np.full(round((2*n-2)), ug)
        Ubh = np.full(round((2*n-2)), uh)
        ub = Ubx.tolist()  + Ubg.tolist() + Ubh.tolist()
        # % f - вектор коэффициентов целевой функции, ненулевыми коэффициентами будут
        # % элементы вектора начиная с(n*n-n)/2+1 до последнего неизвестного
        # % с номером (n*n+7*n)/2-4
        f=np.zeros((int((n*n+7*n)/2-4),1))
        # %Устанавливаем коэффициенты =1 в целевой функции перед всеми переменными - невязками

        for i in  range(round((n*n-n)/2+1), round((n*n+7*n)/2-4)):
            if (i < ((n*n-n)/2+1)+((n*n+7*n)/2-4-(n*n-n)/2)/2):
                f[i] =+ 1
            else:
                f[i] =+ 1
        # % Закончено формирование вектора f
        # % Формируем вектор ограничений вида равенства Aeg - матрицу инцинденций
        # %Начальная инициализация Aeg нулями

        Aeg = np.zeros((round(2*n-2),round((n*n+7*n)/2-4)))
        # % Формируем часть матрицы инциденций по строкам (входам) AegStr, равенства рассчитываются для первых строк (входов) с 1 по n-1
        e=0;
        for i in range(n-1):
            b = e
            e = b+n-i-1
            for j in range(b,e):
                Aeg[i][j] = 1

        # % Формируем часть матрицы инциденций по столбцам (выходам) AegStr, равенства рассчитываются для первых строк (входов) с n по 2*n-2

        for i in range(n-1, (2*n-2)):
            b=i-n+1
            for j in range(i-n+2):
                Aeg[i][b]=1
                b=b+n-j-2
        # % Формируем часть матрицы инциденций по недостатку, рассчитываются для всех строк и столбцов начиная с (n*n-n)/2+2*n-2 по ((n*n-n)/2+2*n-2)+(n-1)

        for i in range(int(2*n-2)):
            j = round(i+(n*n-n)/2+2*n-2)
            Aeg[i][j]=-1

        # % Формируем часть матрицы инциденций по избытку, рассчитываются для всех строк и столбцов начиная с ((n*n-n)/2+2*n-2)+(n-1) по ((n*n-n)/2+2*n-2)+(2*n-2)

        for i in range(2*n-2):
            j = round(i+(n*n-n)/2)
            Aeg[i][j] = 1

        Beq = []
        # % Формируем правые части ограничений вида равенства
        for i in range(2*(n-1)):
            if i <= (n-2):
                Beq.append(A[i])
            else:
                Beq.append(B[i-n+2])
        #%Минимизируем целевую функцию - крупномасштабная оптимизация
        import scipy.optimize as sp
        # from  scipy.optimize import show_options
        #lb # lower bounds
        #ub # upper bounds
        bounds = []
        for i in range(len(lb)):
            bounds.append((lb[i],ub[i]))
        # print(bounds)
        result = sp.linprog(c=f, A_eq=Aeg, b_eq=Beq , bounds=bounds, method=values["robast_method_value"].get(), x0=X0)
        # Востанавливаем полученный вектро X в матрицу корреспонденций
        X1=np.zeros((n,n))
        k=0
        for i in range(n-1):
            for j in range(i+1, n):
                X1[i][j]=result.x[k]
                k=k+1
        X=np.round(X1)
        # Восстанавливаем матрицу перевозок из вектора X
        X1=np.zeros((n,n))
        k=0
        for i in range(n-1):
            for j in range(i+1, n):
                X1[i][j] = result.x[k]
                k=k+1
        # % Невязки по строкам по избытку

        k=0

        for i in range(round((n*n-n)/2+1),round((n*n-n)/2+n-1)):
            H1[k]=result.x[i]
            k=k+1



        H1=np.round(H1)

        # Невязки по столбцам по избытку

        k=0

        for i in range(round((n*n-n)/2+n),round((n*n-n)/2+2*n-2)):
            H2[k]=result.x[i]
            k=k+1


        H2=np.round(H2)


        #  Невязки по строкам по недостаткуу

        k=0
        G1 = []
        for i in range(round((n*n-n)/2+2*n-1),round((n*n-n)/2+3*n-3)):
            G1.append(result.x[i])
            k=k+1


        G1=np.round(G1)

        # Невязки по столбцам по недостатку

        k=0

        for i in range(round((n*n-n)/2+3*n-2),round((n*n-n)/2+4*n-4)):
            G2[k] =result.x[i]
            k=k+1
        G2 = np.round(G2)
        if is_write:
            wtxls.write_to_xls_robast_model(book, X)
        if is_plot:
            plots_data["robast_matrix"] = np.copy(X)
    except Exception as e:
        tk.messagebox.showwarning("Предупреждение", f"Что-то пошло не так! \nОшибка: \n{e}")
