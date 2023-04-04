import os
os.system('cmd /k'"adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
print("Frp done")
