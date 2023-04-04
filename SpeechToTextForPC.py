import speech_recognition as sr
import pyautogui
import winsound

frequency = 2500  # Set the frequency (Hz) of the beep sound
duration = 300  # Set the duration (ms) of the beep sound




while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        winsound.Beep(frequency, duration)
        print("listning ...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            # data = data.lower()Python program to add two values
            pyautogui.write(data)     # Main writer for txt output.
        except sr.UnknownValueError:
            print("Not Understand ")

