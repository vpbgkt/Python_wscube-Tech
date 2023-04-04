import pyautogui
import time
key = pyautogui.press
cmd = pyautogui.typewrite
ContectName = input('Enter the Whatsapp Contect name / Number : ')
Msg = input('Type message here : ')
MsgLoop = int(input('How much times Do you want to send this message ? :'))

print('Wait Dont touch anything')
wait = time.sleep
wait(2)
#
# wait()
key('win')
cmd('whatsapp')
wait(2)
key('enter')
wait(2)
cmd(ContectName)
wait(1)
key('down')
wait(2)
key('enter')

for i in range(MsgLoop+1):
    pyautogui.typewrite(Msg)
    wait(1)
    pyautogui.press("enter")