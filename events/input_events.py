import numpy as np
from tk_root import tk
from global_variables import GLOBAL_VALUES_CONTAINER as values, GLOBAL_LABEL_CONTAINER as labels, GLOBAL_BUTTONS_CONTAINER as buttons, GLOBAL_FRAMES as frames

def keyRelease_long_input(_, input_name):
    divider_value = values["divider_input"].get()
    try:
        labels["count_busstops_label1"].destroy()
        labels["sum1_label"].destroy()
        labels["count_busstops_label1"] = tk.Label(frames["_1subframe1"], text="")
        labels["sum1_label"] = tk.Label(frames["_1subframe1"], text="")
        V = list(map(float, filter(lambda x: x!="", values["long_input1"].get().strip().split(divider_value))))
        labels["count_busstops_label1"]["text"] = f"Количество остановок: {len(V)}"
        labels["sum1_label"]["text"] = f"Сумма: {np.sum(V)}"
        labels["count_busstops_label1"].place(x=10, y=80, anchor='w')
        labels["sum1_label"].place(x=10, y=100, anchor='w')

        labels["count_busstops_label2"].destroy()
        labels["sum2_label"].destroy()
        labels["count_busstops_label2"] = tk.Label(frames["_1subframe1"], text="")
        labels["sum2_label"] = tk.Label(frames["_1subframe1"], text="")
        V = list(map(float, filter(lambda x: x!="", values["long_input2"].get().strip().split(divider_value))))
        labels["count_busstops_label2"]["text"] = f"Количество остановок: {len(V)}"
        labels["sum2_label"]["text"] = f"Сумма: {np.sum(V)}"
        labels["count_busstops_label2"].place(x=10, y=220, anchor='w')
        labels["sum2_label"] .place(x=10, y=240, anchor='w')
    except:
        labels["count_busstops_label1"].destroy()
        labels["sum1_label"].destroy()
        labels["count_busstops_label1"] = tk.Label(frames["_1subframe1"], text="")
        labels["sum1_label"] = tk.Label(frames["_1subframe1"], text="")
        labels["count_busstops_label2"].destroy()
        labels["sum2_label"].destroy()
        labels["count_busstops_label1"] = tk.Label(frames["_1subframe1"], text="")
        labels["sum1_label"] = tk.Label(frames["_1subframe1"], text="")
        labels["count_busstops_label2"] = tk.Label(frames["_1subframe1"], text="")
        labels["sum2_label"] = tk.Label(frames["_1subframe1"], text="")
        labels["count_busstops_label1"]["text"] = f"Количество остановок: 0"
        labels["sum1_label"]["text"] = f"Сумма: 0"
        labels["count_busstops_label2"]["text"] = f"Количество остановок:0"
        labels["sum2_label"]["text"] = f"Сумма: 0"
        labels["count_busstops_label1"].place(x=10, y=80, anchor='w')
        labels["sum1_label"].place(x=10, y=100, anchor='w')
        labels["count_busstops_label2"].place(x=10, y=220, anchor='w')
        labels["sum2_label"].place(x=10, y=240, anchor='w')

def toggle_state_process_btn():
      divider_value = values["divider_input"].get()
      vA = list(map(float, filter(lambda x: x!="", values["long_input2"].get().strip().split(divider_value))))
      vB = list(map(float, filter(lambda x: x!="", values["long_input2"].get().strip().split(divider_value))))
      if len(vA) == len(vB):
          buttons["process_button"].config(state="active")
      else:
          buttons["process_button"].config(state="disabled")
def control_V_keyRelease(_, input_name):
    data = values[input_name].get()
    data_arr = []
    for i in range(len(list(data))):
        if (data[i] >= '0' and data[i] <= '9') or data[i] == " ":
            data_arr.append(data[i])
        else:
            data_arr.append(" ")
    values[input_name].set("".join(data_arr))
    keyRelease_long_input(_, input_name)

def check_correct_spelling(inputname_value):

    data = list(str(values[inputname_value].get()))
    data_arr = []
    temp = 0
    for i in range(len(data)):
        if (data[i] >= '0' and data[i] <= '9'):
            data_arr.append(data[i])
        elif   data[i] == ".":
            if temp == 0:
                data_arr.append(".")
                temp = 1
    values[inputname_value].set("".join(data_arr))





def check_inputs_filling():
    if values["filename_in_value"].get() != "" and values["first_bounds_value"].get() != "" and values["second_bounds_value"].get() != "":
        buttons["add_button"].config(state="active")
    else:
        buttons["add_button"].config(state="disabled")

def handle_input(_, input_name):
    keyRelease_long_input(_, input_name)
    toggle_state_process_btn()
