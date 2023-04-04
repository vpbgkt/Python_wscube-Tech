import webbrowser

import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

listner = sr.Recognizer()
spk = pyttsx3.speak

AssistDB = {'buddy': 'Yeah I am your buddy and i am here for you',
            'how are you': 'I am fine as always.',
            'doing': 'Talking to you',
            'your name': 'My name is vishal',
            'open': '',
            'google': ''
            }


def recognize():
    with sr.Microphone() as source:
        print("Listening...")
        listner.adjust_for_ambient_noise(source)
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command = command.lower()
        return command


def machine(x):
    # print(x + ': in machine function starting.')
    for keys in AssistDB:
        if keys in x and 'google' or 'open' not in x:
            # print(keys)
            print(AssistDB.get(keys))
            break
        if 'open' or 'google' in x:
            print('command from : webbrowser')
            webbrowser.open('https://google.com')
            break
        else:
            continue

    # elif 'search' or 'what is' in command:
    #     print(" command of : wikipedia ")
    #     wikipedia.summary('newton')
    # else:
    #     print('Not understood')




while True:
    try:
        command = recognize()
        machine(command)

    except:
        print('Except occured.............')
