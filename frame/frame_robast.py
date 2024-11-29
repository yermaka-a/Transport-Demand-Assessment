from tk_root import root, tk, ttk
from global_variables import GLOBAL_FRAMES as frames, GLOBAL_VALUES_CONTAINER as values, GLOBAL_ROBAST_METHODS as methods
from frame.subframe_title import subframe_title
def frame_robast(column, row, sticky):
    _3frame1 = tk.Frame(root)
    _3frame1.grid(row=row, column=column, sticky=sticky)
    frames["_3frame1"] = _3frame1
    subframe_title(3)
    _3subframe1 = tk.LabelFrame(_3frame1, relief="solid", bd=2, height=60, width=175, text="Метод расчёта")
    _3subframe1.place(x=10, y=50)
    frames["_3subframe1"] = _3subframe1
    _3frame1.grid_columnconfigure(0, weight=1)
    robast_method_value = tk.StringVar(value="simplex")
    values["robast_method_value"] = robast_method_value
    robast_methods = [ i for i in methods.values()]
    robast_method_lb = ttk.Combobox(_3subframe1, values=robast_methods, textvariable=robast_method_value, state="readonly",  width=18)
    robast_method_lb.place(x=5, y=5)
