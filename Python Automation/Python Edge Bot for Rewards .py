import pyautogui
import time
key = pyautogui.press
wait = time.sleep
HotKey = pyautogui.hotkey
# import pyttsx3
# pyttsx3.speak("Reward Fetching in process please wait and don't touch anything")

# WebSearch = int(input('How much time web search you want to make ? enter number : '))
# MobileSearch = int(input(''' NOTE : To search in mobile in web browser 
# first go to the Microsoft edge browser and 
# do inspect and set screen responsiveness to
# any mobile like : pixel or samsung device 
# How much time web search you want to make ? enter number : '''))
# print("Just wait Don't Touch anything")
WebSearch = 30
MobileSearch = 20
print('******  REQUEST PROCESSING ******')
wait(2)

HotKey('win', 'd')
wait(1)
key('win')
wait(1)
pyautogui.typewrite('edge')
key('enter')
wait(4)
for i in range(0, WebSearch): #for desktop search
    HotKey('ctrl', 'l')
    pyautogui.typewrite(f"{i} Reward Search")
    key('enter')
    wait(2)
HotKey('win', 'up')
HotKey('ctrl', 'shift', 'j')

wait(2)
key('tab')
HotKey('ctrl', 'l')
for i in range(0, MobileSearch+1): #for mobile search
    HotKey('ctrl', 'l')
    pyautogui.typewrite(f"{i} edge browser Mobile Reward Search")
    key('enter')
    wait(2)