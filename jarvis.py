import instaloader
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
import instadownloader



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=30, phrase_time_limit=50)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")


    except Exception as e:
        speak("i dint understand, talk in a human language if u can.")
        return "none"
    return query

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime('%I %M%p')

    if hour>=0 and hour<=12:
        speak(f'Good Morning, its {tt}')
    elif hour>=12 and hour<=18:
        speak(f'Good Afternoon, its {tt}')
    else:
        speak(f'Good Evening, its {tt}')
    speak('I am Jarvis. How can I help you')



    # for news


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6c055aafb67943e48e70c98920e1db6e'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    head = []
    day =['first','second','thrid','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar["title"])
        for i in range (len(day)):
            speak(f'todays {day[i]} news is: {head[i]}')

if __name__ == '__main__':
    wish()
    while True:

        query = take_command().lower()

        # logic building for tasks
        if 'open notepad' in query:
            speak('opening notepad')
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            speak('opening command prompt')
            os.system('start cmd')

        elif 'open camera' in query:
            speak('starting webcam')
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'open minecraft' in query:
            speak('launching minecraft.')
            launcher = "C:\\Users\\gouri\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(launcher)

        elif 'open Fortnite' in query:
            speak('launching fortnite.')
            epic = "C:\\Users\\gouri\\OneDrive\\Desktop\\Fortnite.url"
            os.startfile(epic)

        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            speak(results)

        elif ' open youtube' in query:
            speak('opening youtube')
            webbrowser.open("www.youtube.com")


        elif 'open discord' in query:
            speak('opening discord in browser')
            webbrowser.open("www.discord.com")

        elif 'open whatsapp' in query:
            speak('opening whatsapp in browser')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'open stack overflow' in query:
            speak('opening stack overflow in browser')
            webbrowser.open('www.stackoverflow.com')

        elif 'open google' in query:
            speak('ok, what should I search on google.')
            cm = take_command().lower()
            webbrowser.open(f'{cm}')

        elif 'play youtube' in query:
            song = query.replace('play', '')
            speak('what should i play on youtube')
            speak('playing' + song)
            kit.playonyt(song)

        elif 'thank you' in query:
            speak('youre welcome!')


        elif 'go to bed' in query:
            speak('ok, going to bed')
            sys.exit()

            # to close any app

        elif 'close notepad' in query:
            speak('okay, closing notepad')
            os.system('taskkill /f /im notepad.exe')
            speak('notepad closed')

        elif 'close fortnite' in query:
            speak('okay, closing fortnite')
            os.system('taskkill /f /im Fortnite.url')
            speak('fortnite closed')

        elif 'close minecraft' in query:
            speak('okay, closing minecraft')
            os.system('taskkill /f /im TLauncher.exe')

        #to set alarm

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "C:\\Users\\Default\\Music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        #to find a joke

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shut down' in query:
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep' in query:
            os.system("rundll32.exe powrprof.dll,SendSuspendState 0,1,0")

# to switch window

        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'tell me the news' in query:
            speak('please wait, fetching the latest news')
            news()
#to find location using ip address

        elif 'where am i' in query or 'where are we' in query:
            speak('let me check')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                country = geo_data['country']
                speak(f'i am not sure, but i think we are in {city} and as per my knowledge is in {country}')
            except Exception as e:
                speak('sorry, but i dont think we are on earth.')
                pass

        elif 'check instagram profile' in query:
            speak('please enter the username of the profile')
            name = input('enter username here: ')
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f'here is the profile of user {name}')
            time.sleep(5)
            speak('would u like to download the profile pic of this user?')
            condition = take_command().lower()
        elif 'yes' in query:
            mod = instaloader.Instaloader()
            mod.downlaod_profile(name, profile_pic_only=True)
            speak('download successful')
        else:
            pass
