import psutil 
import time
#imports module for moving the character
import movePlayer_Lite as mp
import keyboard as kb


#pretty sure this can be optimized with asyncio.  ¯\_(ツ)_/¯

#move up and down
print("MovePlayerScript")
def move_up_and_down():
    mp.forward()
    time.sleep(1)
    mp.back()
    time.sleep(4)
    mp.chat("this is a test")

#phantom forces function

# Remember that the order in which the hotkey is set up is the order you
# need to press the keys.

def check_process_status(process_name):
    process_status = [ proc for proc in psutil.process_iter() if proc.name() == process_name ]
    if process_status:
        print(process_status)
    else:
        print("Process name not valid", process_name)
    return process_status
process_status = check_process_status("RobloxPlayerBeta.exe")


count = 0
while 1:
    count = count+1
    print("bot: ",str(count))
    #chat at random times using a random string
    # randomint = randrange(0,10)
    # if randomint == 1:
    #     mp.chat(fc.RandomChatStr())
        
    if kb.is_pressed("space"):
        print("Hotkey is being pressed")
        input()
    
    if kb.is_pressed("k"): #press K to kill
            p = psutil.Process(process_status)
            p.terminate() 

    time.sleep(0.05)
    for current_process in process_status:
        print(current_process.pid)

        
        pidforlib = str(current_process.pid)
        #this code cycles through all the roblox instances by their pid and focuses on the window.
        openlib = r"python RobloxBots\Make-&-join\JoinGame\WindowFocuser\focuslib.py -p " + pidforlib 
        psutil.Popen(openlib)
        time.sleep(4)

        move_up_and_down()

        # mp.chat("-" + str(count)+ " online. ")
        # mp.chat("moveplaterscript")
