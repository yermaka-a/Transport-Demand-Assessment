
from tk_root import tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def plot_in_out(plotsubframe, matrix):
    count_plots = len(matrix)
    half_count =round(count_plots / 2)
    fig, axes = plt.subplots(half_count, half_count+1, figsize=(5 * count_plots, round(4 * half_count)))
    if count_plots == 1:
        axes = [[axes]]
    plt.subplots_adjust(wspace=0.5, hspace=1, top=0.7)

    k = 0
    for j  in range(half_count):
        for i  in range(half_count + 1):

            if k < count_plots:
                axes[j][i].grid(True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)
                axes[j][i].bar([i + 1 for i in range(len(matrix[i]))],matrix[k])
                axes[j][i].set_xlabel(f"Остановка {k + 1}")

            else:
                axes[j][i].set_visible(False)
            k += 1
    fig.suptitle("Структура корреспонденций прибывающего пассажиропотока \n по остановкам", fontsize=16, y=0.9)
    canvas = FigureCanvasTkAgg(fig, master=plotsubframe)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH)
