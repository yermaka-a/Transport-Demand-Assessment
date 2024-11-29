import matplotlib.pyplot as plt
import numpy as np
from global_variables import GLOBAL_GRAPHICS_CONTAINER as graphics
 # Пример отрисовки графика
def plot_graph(canvas, x, y):
    # Создаем данные для графика
    # Очищаем предыдущий график
    for i in range(len(graphics[0])):
        print(i)
        graphics[0][i].clear()
        if i == 0:
            graphics[0][i].set_title("Входы(выборка 1)")
            graphics[0][i].bar([ i+1 for i in range(len(x))],x)
        if i == 1:
            graphics[0][i].set_title("Выходы(Выборка 2)")
            graphics[0][i].bar([ i+1 for i in range(len(y))],y)

        graphics[0][i].set_xlabel("номер остановки")
        graphics[0][i].set_ylabel("Кол-во")

    # Обновляем канвас
    canvas.draw()
