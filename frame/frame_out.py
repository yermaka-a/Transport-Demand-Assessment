from global_variables import GLOBAL_VALUES_CONTAINER as values, GLOBAL_FRAMES as frames
from frame.subframe_title import subframe_title
from tk_root import tk, root, ttk
def frame_out(column, row, sticky):
    _4frame1 = tk.Frame(root)
    _4frame1.grid(row=row, column=column, sticky=sticky)
    frames["_4frame1"] = _4frame1
    subframe_title(4)
    _4subframe1 = tk.Frame(_4frame1, relief="solid", bd=2, height=300)
    _4subframe1.grid(row=1, column=0,  sticky="snew", columnspan=3)
    frames["_4subframe1"] = _4subframe1
    _4frame1.grid_columnconfigure(0, weight=1)

    filename_out_lbl = tk.Label(_4subframe1, text="Имя файла")
    filename_out_lbl.place(x=10,y=15, anchor="w")
    filename_out_value = tk.StringVar()
    filename_out_inp = tk.Entry(_4subframe1, textvariable=filename_out_value)
    values["filename_out_value"] = filename_out_value
    filename_out_inp.place(x=10,y=40, anchor="w")
    autonum_files_lbl = tk.Label(_4subframe1, text="Автоматическая нумерация")
    autonum_files_lbl.place(x=10,y=70, anchor="w")
    autonum_files_value = tk.BooleanVar(value=1)
    values["autonum_files_value"] = autonum_files_value
    autonum_files_chkbtn = tk.Checkbutton(_4subframe1, variable=autonum_files_value, text="")
    autonum_files_chkbtn.place(relx=0.29, rely=0.24, anchor="w")
