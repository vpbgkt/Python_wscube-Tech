import os
while True:
    os.system('cmd /c "adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1"')
    print("""Frp done if mobile connected with adb enabled 
          and Usb debugging allowed. 
          Else check and try agian""")
    ch = input("Do you want to exit now ? (y/n):  ")
    if ch == "y":
        break
    else:
        print("Wrong input or select another choice:")

