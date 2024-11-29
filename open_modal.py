from tk_root import tk, ttk, root
from frame.frame_tree import create_treeview
from frame.frame_source_data import frame_source_data
from frame.frame_buttons import frame_buttons
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# import matplotlib.pyplot as plt
# from choose_calculate_type import choose_calculate_type
# # from plot import plot_graph
from events.input_events import keyRelease_long_input
from global_variables import GLOBAL_VALUES_CONTAINER as GLOBAL_VALUES, GLOBAL_LABEL_CONTAINER, GLOBAL_BUTTONS_CONTAINER, GLOBAL_INPUTS_CONTAINER as GLOBAL_INPUTS, GLOBAL_COUNT_OF_CONTAINER, GLOBAL_BOXES_CONTAINER, GLOBAL_GRAPHICS_CONTAINER as graphics, GLOBAL_SCROLLS_CONTAINER as scrolls, GLOBAL_EVENTS_CONTAINER as events,  GLOBAL_TREE, GLOBAL_FRAMES as frames
from closing import on_closing
from frames_recovery.frames_recovery import frame_recovery
from frame.frame_gravit import frame_gravit
from frame.frame_robast import frame_robast
from frame.frame_out import frame_out
def on_tree_select(e):
    if e != None:
        selected_id = e.widget.selection()[0]
    else:
        selected_id = '1'
# Скрываем все фреймы
    for frame in frames.values():
        frame.grid_remove()

    # Показываем фрейм, соответствующий выбранному элементу
    frame_recovery(selected_id)


root.title("Оценка транспортного спроса")
root.geometry("800x600")
# создание TreeView
create_treeview(0, 0, "nsew")
# notebook = ttk.Notebook(root)
# notebook.grid(column=1,row=0)
# создаем фрейм для ввода исходных данных
frame_source_data(1,0, "nsew")
frame_gravit(1,0, "nsew")
frame_robast(1, 0, "nsew")
frame_out(1, 0, "nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)



# фрейм для кнопок
frame_buttons(0, 1, "nsew")
keyRelease_long_input(0, "long_input1")
keyRelease_long_input(0, "long_input2")

GLOBAL_TREE["global_tree"].bind('<<TreeviewSelect>>', lambda e: on_tree_select(e))
on_tree_select(None)
root.protocol("WM_DELETE_WINDOW", on_closing)
