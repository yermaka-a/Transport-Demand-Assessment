
from global_variables import GLOBAL_VALUES_CONTAINER as values, GLOBAL_INPUTS_CONTAINER as inputs, GLOBAL_FRAMES as frames, GLOBAL_BUTTONS_CONTAINER as buttons
from tk_root import tk, root, ttk
from events.input_events import check_inputs_filling
from xls.get_data_from_xls import get_data_from_xls
def open_xls_inputs(_):
    if(values["value_of_checkBox_inputsource"].get() == 1):
        for widget in frames["_1subframe2"].winfo_children():
            if isinstance(widget, tk.Label):
                if widget["text"] == "Ввод с EXCEL файла:":
                    continue
            if isinstance(widget, ttk.Checkbutton):
                continue
            widget.place_forget()
    elif(values["value_of_checkBox_inputsource"].get() == 0):
            file_lbl_xls = tk.Label(frames["_1subframe2"], text="Имя файла:")
            file_lbl_xls.place(x=10,y=45, anchor="w")
            filename_in_value = tk.StringVar()
            values["filename_in_value"] = filename_in_value
            file_inp_xls = tk.Entry(frames["_1subframe2"], textvariable=filename_in_value)
            file_inp_xls.place(x=10,y=66, anchor="w")
            file_inp_xls.bind("<KeyRelease>", lambda e: check_inputs_filling())

            _1_2lbframe1 = ttk.Labelframe(frames["_1subframe2"], text="Диапазон ячеек")
            _1_2lbframe1.place(x=10, y=145, relwidth=0.9, relheight=0.4,  anchor='w')
            frames["_1_2lbframe1"] = _1_2lbframe1
            first_lbl_xls = tk.Label(frames["_1_2lbframe1"], text="Вошедшие пассажиры")
            first_lbl_xls.place(x=10,y=10, anchor="w")
            first_bounds_value = tk.StringVar()
            values["first_bounds_value"] = first_bounds_value
            first_inp_xls = tk.Entry(frames["_1_2lbframe1"], textvariable=first_bounds_value)
            first_inp_xls.place(x=10,y=30, anchor="w", relwidth=0.9)
            first_inp_xls.bind("<KeyRelease>", lambda e: check_inputs_filling())

            second_lbl_xls = tk.Label(frames["_1_2lbframe1"], text="Вышедшие пассажиры")
            second_lbl_xls.place(x=10,y=60, anchor="w")
            second_bounds_value = tk.StringVar()
            values["second_bounds_value"] = second_bounds_value
            second_inp_xls = tk.Entry(frames["_1_2lbframe1"], textvariable=second_bounds_value)
            second_inp_xls.place(x=10,y=80, anchor="w", relwidth=0.9)
            second_inp_xls.bind("<KeyRelease>", lambda e: check_inputs_filling())
            add_button = tk.Button(frames["_1subframe2"], text="Добавить", state="disabled", command=lambda:get_data_from_xls())
            add_button.place(relx=0.25, rely=0.7)
            buttons["add_button"] = add_button
