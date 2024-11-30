from tk_root import tk, ttk
from global_variables import GLOBAL_FRAMES as frames, GLOBAL_PLOTSDATA as plots_data
from forms.plot_in_out import plot_in_out
def plot_note_frame1():
    plotsubnote1 = ttk.Notebook(frames["note_frame1"])
    plotsubnote1.pack(expand=True, fill=tk.BOTH)
    plotsubframe1 = ttk.Frame(plotsubnote1)
    plotsubframe2 = ttk.Frame(plotsubnote1)
    plotsubframe1.pack(expand=True, fill=tk.BOTH, anchor='w')
    plotsubframe2.pack(expand=True, fill=tk.BOTH)
    plotsubnote1.add(plotsubframe1, text="Гравитационная модель")
    plotsubnote1.add(plotsubframe2, text="Робастная модель")
    frames["note_frame1"].grid_rowconfigure(0, weight=1)
    frames["note_frame1"].grid_columnconfigure(0, weight=1)
    corr_matrix_T = plots_data["corr_matrix"].T
    robast_matrix_T = plots_data["robast_matrix"].T
    plot_in_out(plotsubframe1, corr_matrix_T)
    plot_in_out(plotsubframe2, robast_matrix_T)
