from django.shortcuts import render,HttpResponse,redirect
import datetime
import operator
import os
import webbrowser
import wikipedia
import wolframalpha
import pyttsx3
import speech_recognition as beta
import datetime
import json
import operator
import os
from urllib import request
import webbrowser
import wikipedia
import pyjokes
import wolframalpha
import pyttsx3
from urllib.request import urlopen



# Create your views here.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def home(request):
    return HttpResponse('This is the main page!')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Giya 1 point o")
    speak("I am your Assistant")


def assistant(request):
    cmd = 'Give the command'
    if request.method == 'POST':
        cmd = request.POST['cmd']
        res = evaluate(cmd)
    return render(request,'base.html',{'cmd':cmd,'res':res})

def evaluate(query):
    query.lower()
# Youtube
    if 'open youtube' in query or 'open YouTube' in query:
        # speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        # os.system('cls')
# Wikipedia
    elif 'wikipedia' in query or 'Wikipedia' in query :
        # speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        # speak("According to Wikipedia")
        # speak(results)
        return (results)
        # os.system('cls')
# Google
    elif 'open google' in query:
            # speak("Here you go to Google\n")
            webbrowser.open("google.com")
            # os.system('cls')
# Stack Overflow
    elif 'open stack overflow' in query:
        # speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
        # os.system('cls')
# Instagram
    elif 'open instagram' in query:
        # speak("Here you go to Instagram")
        webbrowser.open("instagram.com")
        # os.system('cls')
# Joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        speak(joke)
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

    elif 'when' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('when')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer

    elif 'why' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('how')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
    
    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif "who i am" in query:
        return ("If you talk then definitely your human.")
    # return None

def test(request):
    res = 'Give the command'
    if (request.method == "POST"):
        cmd = request.POST['cmd']
        
    return render(request,'testing.html',{'res':res,'cmd':cmd,})


