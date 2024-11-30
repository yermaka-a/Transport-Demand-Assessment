from tk_root import tk, ttk, root
from global_variables import GLOBAL_FRAMES as frames, GLOBAL_PLOTSDATA as plots_data
from forms.note_frame1 import plot_note_frame1
from forms.note_frame2 import plot_note_frame2
def create_plot_form():
    plot_form = tk.Toplevel(root)
    plot_form.title("Графики")
    plot_form.geometry("800x600")
    # plot_form.protocol("WM_DELETE_WINDOW", lambda: plot_form.destroy())
    plt_notebook = ttk.Notebook(plot_form)
    plt_notebook.pack(expand=True, fill=tk.BOTH)
    note_frame1 = ttk.Frame(plt_notebook)
    note_frame2 = ttk.Frame(plt_notebook)
    note_frame3 = ttk.Frame(plt_notebook)
    note_frame1.pack(expand=True, fill=tk.BOTH, anchor='w')
    note_frame2.pack(expand=True, fill=tk.BOTH)
    note_frame3.pack(expand=True, fill=tk.BOTH)
    plt_notebook.add(note_frame1, text="Структура прибывающего")
    plt_notebook.add(note_frame2, text="Структура убывающего")
    plt_notebook.add(note_frame3, text="Ошибка")
    frames["note_frame1"] = note_frame1
    frames["note_frame2"] = note_frame2
    frames["note_frame3"] = note_frame3
    print(plots_data.keys())
    print(plots_data.values())
    plot_note_frame1()
    plot_note_frame2()
