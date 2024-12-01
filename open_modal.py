import os
from tk_root import root
from events.input_events import handle_input
from global_variables import GLOBAL_VALUES_CONTAINER as GLOBAL_VALUES, GLOBAL_TREE, GLOBAL_FRAMES as frames
from closing import on_closing
from frame.frame_tree import create_treeview
from frame.frame_source_data import frame_source_data
from frame.frame_buttons import frame_buttons
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
if not os.path.isdir("./Исходные данные"):
    os.mkdir("./Исходные данные")
if not os.path.isdir("./Вывод данных"):
    os.mkdir("./Вывод данных")
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
handle_input(0, "long_input1")
handle_input(0, "long_input2")

GLOBAL_TREE["global_tree"].bind('<<TreeviewSelect>>', lambda e: on_tree_select(e))
on_tree_select(None)
print(GLOBAL_VALUES.keys())
root.protocol("WM_DELETE_WINDOW", on_closing)
print(frames.keys())
