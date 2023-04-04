import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit

listner = sr.Recognizer()
spk = pyttsx3.speak
print('''>>>>>>> INSTRUCTIONS and Features >>>>>>>
[Always call me by vishal name and to ]
    1. Vishal play 'Song name'.
    2. Vishal who is 'person name' [Search on wikipedia].
    3. Vishal search 'Android' on wikipedia [Wikipedia search].
    4. Vishal open Google.
    5. Vishal how are you, what are you doing, What is your name;
    6. Use 'Bye' or 'Exit' to terminate program
    [You can add your own command in Dictionary with key and value pair]
    
    @copyright Devloper-Vishal vpbgkt@gmail.com
''')

assistdb = {'buddy': 'Yeah I am your buddy and i am here for you',
            'how are you': 'I am fine as always.',
            'doing': 'Talking to you',
            'your name': 'My name is vishal',
            }


# Function defination part
def recognize():
    with sr.Microphone() as source:
        print("Listening...")
        listner.adjust_for_ambient_noise(source)
        voice = listner.listen(source)
        usercmd = listner.recognize_google(voice)
        usercmd = usercmd.lower()
        return usercmd


def assist(usercmd):
    if 'on youtube' or 'in youtube' or 'youtube' or 'song' in usercmd:
        usercmd = usercmd.replace('youtube', ' ')
        usercmd = usercmd.replace('in youtube', ' ')
        usercmd = usercmd.replace('on youtube', ' ')

    for i in assistdb:
        if i in usercmd:
            print('Output: ' + assistdb.get(i))
            spk(assistdb.get(i))
            break
        elif 'open' and 'google' in usercmd:
            webbrowser.open('google.com')
            spk('Opened in browser')

    if 'play' in usercmd:

        usercmd = usercmd.replace('play', ' ')
        usercmd = usercmd.replace('vishal', ' ')
        print('Output:' + usercmd)
        spk('playing' + usercmd + 'on youtube')
        pywhatkit.playonyt(usercmd)
    # elif 'wikipedia' or 'search' or 'who is'in usercmd:
    #     usercmd=usercmd.replace('vishal', ' ')
    #     usercmd=usercmd.replace('wikipedia', ' ')
    #     usercmd=usercmd.replace('search', ' ')
    #     usercmd=usercmd.replace('on', ' ')
    #     wiki = wikipedia.summary(usercmd, 2)
    #     print(wiki)
    #     spk(wiki)

spk("Hello. I am vishal your assistant if you are having any work then just say any command with my name vishal")

while True:
    try:
        usercmd = recognize()
        # if 'exit' or 'bye' in usercmd:
        #     break
        if 'vishal' in usercmd:
            print(usercmd)
            assist(usercmd)
        else:
            continue
    except:
        print(usercmd)
        print('OUTPUT : Try agian... ')
        # pyttsx3.speak("No command given")
