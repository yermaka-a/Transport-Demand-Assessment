from tk_root import tk, root, ttk
from global_variables import  GLOBAL_VALUES_CONTAINER as GLOBAL_VALUES, GLOBAL_LABEL_CONTAINER as labels, GLOBAL_FRAMES as frames, GLOBAL_INPUTS_CONTAINER as inputs
from events.input_events import handle_input, control_V_keyRelease
from events.buttons_events import open_xls_inputs
from frame.subframe_title import subframe_title
def frame_source_data(column, row, sticky):
    example_aV = [9, 13, 7, 2, 0]
    example_bV = [0, 5, 4, 7, 15]
    try:
        long_input1_var = GLOBAL_VALUES["long_input1"]
        long_input2_var = GLOBAL_VALUES["long_input2"]
    except:
        long_input1_var = tk.StringVar(value=" ".join(map(str, example_aV)))
        long_input2_var = tk.StringVar(value=" ".join(map(str, example_bV)))
        GLOBAL_VALUES["long_input1"] = long_input1_var
        GLOBAL_VALUES["long_input2"] = long_input2_var
    divider_var = tk.StringVar(value=" ")
    value_of_checkBox_inputsource = tk.BooleanVar(value=False)

    GLOBAL_VALUES["divider_input"] = divider_var
    GLOBAL_VALUES["value_of_checkBox_inputsource"] = value_of_checkBox_inputsource
    _1frame1 = tk.Frame(root)
    _1frame1.grid(row=row, column=column, sticky=sticky)
    frames["_1frame1"] = _1frame1
    subframe_title(1)
    _1subframe1 = tk.Frame(_1frame1, relief="solid", bd=2, width=400, height=320)
    _1subframe1.grid(row=1, column=0,  sticky="nwe", columnspan=2)
    _1subframe2 = tk.Frame(_1frame1, relief="solid", bd=2, width=200, height=320)
    _1subframe2.grid(row=1, column=1,  sticky="nwe")
    # frame1.grid_rowconfigure(0, weight=1)
    _1frame1.grid_rowconfigure(1, weight=1)
    _1frame1.grid_columnconfigure(0, weight=1)
    frames["_1subframe1"] = _1subframe1
    frames["_1subframe2"] = _1subframe2

    # Длинные инпуты с прокруткой
    long_input1_label = tk.Label(_1subframe1, text="Количество вошедших пассажиров:")
    long_input1_label.place(x=10, y=15, anchor='w')

    long_input1_frame = ttk.Frame(_1subframe1)
    long_input1_frame.place(x=10, y=30, relwidth=0.63)
    long_input1_scroll = ttk.Scrollbar(long_input1_frame, orient='horizontal')
    long_input1_scroll.pack(side='bottom', fill='x')
    long_input1 = tk.Entry(long_input1_frame, textvariable=long_input1_var)
    long_input1.pack(side='left', fill='x', expand=True)
    long_input1_scroll.config(command=long_input1.xview)
    long_input1.config(xscrollcommand=long_input1_scroll.set)
    inputs["long_input1"] = long_input1

    count_busstops_label1 = tk.Label(_1subframe1, text="Количество остановок:")
    count_busstops_label1.place(x=10, y=80, anchor='w')
    sum1_label = tk.Label(_1subframe1, text="Сумма:")
    sum1_label.place(x=10, y=100, anchor='w')
    labels["count_busstops_label1"] = count_busstops_label1
    labels["sum1_label"] = sum1_label

    long_input2_label = tk.Label(_1subframe1, text="Количество вышедших пассажиров:")
    long_input2_label.place(x=10, y=140)


    long_input2_frame = ttk.Frame(_1subframe1)
    long_input2_frame.place(x=10, y=170, relwidth=0.63)
    long_input2_scroll = ttk.Scrollbar(long_input2_frame, orient='horizontal')
    long_input2_scroll.pack(side='bottom', fill='x')

    long_input2 = tk.Entry(long_input2_frame, textvariable=long_input2_var)
    long_input2.pack(side='left', fill='x', expand=True)
    long_input2_scroll.config(command=long_input2.xview)
    long_input2.config(xscrollcommand=long_input2_scroll.set)
    inputs["long_input2"] = long_input2
    _1subframe1.grid_columnconfigure(0, weight=1)

    count_busstops_label2 = tk.Label(_1subframe1, text="Количество остановок:")
    count_busstops_label2.place(x=10, y=220, anchor='w')
    sum2_label = tk.Label(_1subframe1, text="Сумма:")
    sum2_label.place(x=10, y=240, anchor='w')
    labels["count_busstops_label2"] = count_busstops_label2
    labels["sum2_label"] = sum2_label

    divider_input = tk.Entry(_1subframe1, textvariable=divider_var, width=3)
    divider_input.place(x=10, y=290, anchor='w')
    divider_label = tk.Label(_1subframe1, text="Разделитель значений")
    divider_label.place(x=50, y=290, anchor='w')
    inputs["divider_input"] = divider_input

    long_input1.bind("<KeyRelease>", lambda e: handle_input(e, "long_input1"))
    long_input2.bind("<KeyRelease>", lambda e: handle_input(e, "long_input2"))
    divider_input.bind("<KeyRelease>",lambda e: handle_input(e, "long_input2"))

    # count_of_iter_input.bind("<KeyRelease>",lambda e: keyRelease_long_input(e, "long_input2"))

    GLOBAL_VALUES["long_input1"].trace_add(mode=('write'), callback=lambda name, i, mode: control_V_keyRelease(i, "long_input1"))
    GLOBAL_VALUES["long_input2"].trace_add(mode=('write'), callback=lambda  name, i, mode: control_V_keyRelease(i, "long_input2"))


    input_from_xlsx_label = tk.Label(_1subframe2, text="Ввод с EXCEL файла:")
    input_from_xlsx_label.place(x=10,y=15, anchor="w")
    input_from_checkbtn = tk.Checkbutton(_1subframe2, variable=value_of_checkBox_inputsource)
    input_from_checkbtn.place(relx=0.65, rely=0.06,anchor="w")
    input_from_checkbtn.bind("<ButtonRelease>", lambda e: open_xls_inputs(e))
