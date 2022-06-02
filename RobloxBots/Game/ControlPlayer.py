import pydirectinput as pdi
# import win32gui as wg

#presses the W key to move character forwords 
def forward():
        pdi.press("w")
#presses the S key to move character backwords
def back():
     pdi.press("s")


def left():
     pdi.press("a")

def right():
     pdi.press("d")
#type string into the chat
def chat(chatstring):
        pdi.press('/')
        pdi.write(chatstring)
        pdi.press('enter')

#MiscellaneousCharacters
# class MiscellaneousCharacters(object):

#phantom forces specific
class PhantomFoces(object):
    def __init__(self):
        pass
#deploy into battle
    @staticmethod
    def Deploy():
        pdi.press('space')

#initiate a vokekick
    @staticmethod
    def VKInit(player,reason):
        def colon():
            pdi.keyDown("shift")
            pdi.press(";")
            pdi.keyUp("shift")

        pdi.write('/votekick')
        colon()
        pdi.write(player)
        colon()
        pdi.write(reason)
        pdi.press("enter")
        
    #vote in a vokekick
    @staticmethod
    def VK(YesNo):
        """vote in a vote kick duh"""
        pdi.press(YesNo)

    #spot enemey 
    @staticmethod
    def spot():
        
        pdi.press('e')
    


        
