from tk_root import root, tk, ttk
from global_variables import GLOBAL_FRAMES as frames, GLOBAL_VALUES_CONTAINER as values
from frame.subframe_title import subframe_title
def frame_gravit(column, row, sticky):
    _2frame1 = tk.Frame(root)
    _2frame1.grid(row=row, column=column, sticky=sticky)
    frames["_2frame1"] = _2frame1
    subframe_title(2)
    _2subframe1 = tk.Frame(_2frame1, relief="solid", bd=2, height=300)
    _2subframe1.grid(row=1, column=0,  sticky="snew", columnspan=3)
    frames["_2subframe1"] = _2subframe1

    _2frame1.grid_columnconfigure(0, weight=1)


    iter_label = tk.Label(_2subframe1, text="Количество итераций:")
    iter_label.place(relwidth=0.25, x=10, y=20,anchor='w')
    count_of_iter = tk.IntVar(value=100)
    iter_input = tk.Entry(_2subframe1, textvariable=count_of_iter)
    iter_input.place(relwidth=0.2, x=10, y=50,  anchor='w')

    accuracy_lbl = tk.Label(_2subframe1, text="Точность:")
    accuracy_lbl.place(relwidth=0.2, x=10, y=85,anchor='w')
    accuracy_value = tk.DoubleVar(value=0.001)
    iter_input = tk.Entry(_2subframe1, textvariable=accuracy_value)
    iter_input.place(relwidth=0.2, x=10, y=110,  anchor='w')
    gravit_out_value_text = tk.StringVar(value="Вывод гравитационной модели")
    gravit_out_value = tk.BooleanVar(value=True)
    gravit_radiobtn_out = tk.Checkbutton(_2subframe1, textvariable=gravit_out_value_text, variable=gravit_out_value)
    gravit_radiobtn_out.place( y=140,  anchor='w')
    values["gravit_out_value"] = gravit_out_value
    values["gravit_out_value_text"] = gravit_out_value_text
    iter_label = tk.Label(_2subframe1, text="итерации от")
    iter_label.place(x=10, y=165,anchor='w')
    count_of_iter_start = tk.IntVar(value=1)
    count_of_iter_end = tk.IntVar(value=100)
    values["count_of_iter_start"] = count_of_iter_start
    values["count_of_iter_end"] = count_of_iter_end
    iter_input_start = tk.Entry(_2subframe1, textvariable=count_of_iter_start)
    iter_input_start.place(relwidth=0.1, x=len("итерации от")*9, y=165,  anchor='w')
    iter_label = tk.Label(_2subframe1, text="до")
    iter_label.place(x=len("итерации от")*15, y=165,anchor='w')
    iter_input_end = tk.Entry(_2subframe1, textvariable=count_of_iter_end)
    iter_input_end.place(relwidth=0.1, x=len("итерации от")*17, y=165,  anchor='w')
