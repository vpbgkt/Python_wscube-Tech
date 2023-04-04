
import pyautogui
import time
Total_stocks = int(input('How much stocks do you wanna view ? : '))
stock = []
database = {'axis bank': 'axisbank',
            'hdfc bank': 'hdfcbank'
            }

for i in range(1, Total_stocks+1):

    stock.append(input(f'Enter the stock name {i} : '))


time.sleep(1)
pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite('brave')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

for i in range(0, len(stock)):
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite(f'https://www.tradingview.com/chart/L5myLa8E/?symbol=NSE%3A{stock[i]}')
    pyautogui.press('enter')
    time.sleep(4)
    if i == len(stock)-1:
        break
    else:
        pyautogui.hotkey('ctrl', 't')


    # time.sleep(1)

