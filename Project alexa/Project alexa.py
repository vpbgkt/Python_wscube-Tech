import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit

listner = sr.Recognizer()

spk = pyttsx3.speak
spk("Hello.")

assistdb = {'buddy': 'Yeah I am your buddy and i am here for you',
            'how are you': 'I am fine as always.',
            'doing': 'Talking to you',
            'alexa': 'Hello! i am Here. how can i help you'

            }


# Function defination part
def recognize():
    with sr.Microphone() as source:
        print("Listning...")
        voice = listner.listen(source)
        usercmd = listner.recognize_google(voice)
        usercmd = usercmd.lower()
        return usercmd


def assist(usercmd):
    usercmd = usercmd.removeprefix('alexa')
    usercmd = usercmd.removeprefix('play')
    if 'buddy' in usercmd:
        spk(assistdb.get('buddy'))

    elif 'how are you' in usercmd:
        spk(assistdb.get('how are you'))
    elif 'doing' in usercmd:
        spk(assistdb.get('doing'))
    elif 'open' and 'google' in usercmd:
        webbrowser.open('google.com')
        spk('Opened in browser')
    elif 'play' in usercmd:
        

        print(usercmd)
        pywhatkit.playonyt(usercmd)


while True:
    try:
        usercmd = recognize()
        if 'alexa' in usercmd:
            print(usercmd)
            assist(usercmd)
        else:
            continue

    except:
        print('No command given')
        # pyttsx3.speak("No command given")
