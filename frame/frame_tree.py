from tk_root import root, tk, ttk
from global_variables import GLOBAL_TREE
def create_treeview(column, row, sticky):
    tree = ttk.Treeview(root, show="tree")
    choosing_name = ["Ввод исходных данных", "Настройка гравитационной модели", "Настройка робастной модели", "Вывод данных" ]

    # добавляем отделы
    tree.tag_configure('lightgrey', background="lightgrey", )
    tree.tag_configure('lightblue', background="#AEC6CF")
    tree.insert("", tk.END, iid=1, text=choosing_name[0], tags=('lightblue'))
    tree.insert("", tk.END, iid=2, text=choosing_name[1], tags=('lightgrey'))
    tree.insert("", tk.END, iid=3, text=choosing_name[2], tags=('lightblue'))
    tree.insert("", tk.END, iid=4, text=choosing_name[3], tags=('lightgrey'))
    tree.grid(column=column,row=row, sticky=sticky)
    tree.selection_set('1')
    GLOBAL_TREE["global_tree"] = tree
