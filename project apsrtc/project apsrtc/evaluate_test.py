import datetime
import json
import operator
import os
from urllib import request
import webbrowser
import wikipedia
import pyjokes
from googlesearch import search
import wolframalpha
import pyttsx3
from urllib.request import urlopen
import speech_recognition as beta

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def evaluate(query):
    query.lower()
# Youtube
    if 'open youtube' in query or 'open YouTube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        # os.system('cls')
# Wikipedia
    elif 'wikipedia' in query or 'Wikipedia' in query :
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        speak(results)
        return (results)
        # os.system('cls')
# Google
    elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
            # os.system('cls')
# Stack Overflow
    elif 'open stack overflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
        # os.system('cls')
# Instagram
    elif 'open instagram' in query:
        speak("Here you go to Instagram")
        webbrowser.open("instagram.com")
        # os.system('cls')
# Joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        return (joke)
        # os.system('cls')
# Time
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        # speak(f"Sir, the time is {strTime}")
        return(strTime)
        # print('\n')
# Calculate
    elif "calculate" in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        # speak("The answer is " + answer)
        return answer
# What
    elif 'what' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('what')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        # speak("The answer is " + answer)
        return answer
# Who
    elif 'who' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('who')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        # speak("The answer is " + answer)
        return answer
# Where
    elif 'where' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('where')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
# When
    elif 'when' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('when')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
# Why
    elif 'why' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('how')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
# Search
    elif 'search' in query or 'play' in query :
        query = query.replace("search for", "")
        query = query.replace("search", "")
        query = query.replace("google", "")
        query = query.replace("play", "")
        webbrowser.open(query)

        return "Here what I found on Internet"
# Google
    elif 'google' in query:
        query = query.replace("google", "")
        search_results = search(query, 10)
        return search_results

    elif "who i am" in query:
        return ("If you talk then definitely your human.")
    
    elif 'exit' in query or 'close' in query:
            speak("Thanks for giving me your time")
            exit()
    
    return None


def takeCommand():
    os.system('cls')
    r = beta.Recognizer()
    my_mic_device = beta.Microphone(device_index=1)

    with my_mic_device as source:
        print("Listining!!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return None

    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

os.system('cls')
wishMe()
while True:
    cmd = takeCommand()
    os.system('cls')

    if not cmd is None:
        print(cmd.lower())
        print()
        res = evaluate(cmd.lower())

        if not res is None:
            print(res)
            speak(res)
        else:
            print("Sorry! I couldn't find it")
            speak("sorry I couldn't find it")


    else:
        print("Sorry I didn't get it")
        speak("Sorry I didn't get it")