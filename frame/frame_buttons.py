from tk_root import root, tk, ttk
from global_variables import GLOBAL_BUTTONS_CONTAINER as buttons
from choose_calculate_type  import choose_calculate_type
def frame_buttons(column, row, sticky):
    frame_buttons = tk.Frame(root, bg="#AEC6CF", height=40)
    frame_buttons.grid(row=row, column=column, sticky=sticky, columnspan=2)


    process_button = tk.Button(frame_buttons, text="Рассчитать", state="disabled", command=lambda: choose_calculate_type())
    process_button.place(relx=0.86, rely=0.1)
    buttons["process_button"] = process_button
    plots_button = tk.Button(frame_buttons, text="Графики", state="disabled", command=lambda: choose_calculate_type())
    plots_button.place(relx=0.74, rely=0.1)
    buttons["plots_button"] = plots_button
