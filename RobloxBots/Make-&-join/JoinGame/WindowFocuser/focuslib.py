import win32gui
import win32process
import argparse

#cylces through the roblox pids so pyinput library can controll each player one by one. 


#  This is black magic
#  !!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!

ap=argparse.ArgumentParser()
ap.add_argument("-p", "--pid", type=int, required=True,help="the pid")

args=vars(ap.parse_args())
pids = args["pid"]

def enum_window_callback(hwnd, pid):
    # i dont know how or why but it just works
    a,current_pid = win32process.GetWindowThreadProcessId(hwnd) # wtf is that 'a' just hanging around there?
    # print(pid)
    # print(current_pid)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        print("window activated") 
    

win32gui.EnumWindows(enum_window_callback,pids)
#!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!!!!!!DO NOT TOUCH!!!!