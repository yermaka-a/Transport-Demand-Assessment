from tk_root import root, tk, ttk
from global_variables import GLOBAL_FRAMES as frames, GLOBAL_TREE as tree
def subframe_title(item_id):

    subframe_title = tk.Frame(frames[f"_{item_id}frame1"], relief="solid", bd=1)
    subframe_title.grid(column=0, sticky="nwe", columnspan=3)

    title_label = tk.Label(subframe_title, text=f"{tree["global_tree"].item(item_id)['text']}", font=("Helvetica", 16))
    title_label.pack(padx=10, pady=10, anchor="w", expand=1)
