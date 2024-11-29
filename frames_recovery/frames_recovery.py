from global_variables import GLOBAL_FRAMES as frames

def frame_recovery(i):
    if i == '1':
        frames[f"_{i}frame1"].grid()
        frames["_1subframe1"].grid()
        frames["_1subframe2"].grid()
    elif i == '2':
         frames[f"_{i}frame1"].grid()
         frames[f"_{i}subframe1"].grid()
    elif i == '3':
        frames[f"_{i}frame1"].grid()
        frames[f"_{i}subframe1"].place()
    elif i == '4':
        frames[f"_{i}frame1"].grid()
        frames[f"_{i}subframe1"].grid()
