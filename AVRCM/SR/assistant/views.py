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
from googlesearch import search
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
    res = ''
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
    elif 'wikipedia' in query or 'Wikipedia about' in query :
        # speak('Searching Wikipedia...')
        query = query.replace("wikipedia about", "")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences = 2)
        # speak("According to Wikipedia")
        # speak(result)
        return (result)
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
        return (joke)
        # os.system('cls')
# News
    elif 'news' in query:
                    try:
                        jsonObj = urlopen(
                            '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                        data = json.load(jsonObj)
                        i = 1

                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============''' + '\n')

                        for item in data['articles']:
                        
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:
                    
                        print(str(e))
# Weather
    # elif "weather" in query:
    #     # Google Open weather website
    #     # to get API of Open weather
    #     api_key = "404f1521f7ee16569f6a1d8875393578"
    #     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #     speak(" City name ")
    #     print("City name : ")
    #     city_name = takeCommand()
    #     complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    #     response = request.Request(complete_url)
    #     x = response.json()

    #     if x["code"] != "404":
    #         y = x["main"]
    #         current_temperature = y["temp"]
    #         current_pressure = y["pressure"]
    #         current_humidiy = y["humidity"]
    #         z = x["weather"]
    #         weather_description = z[0]["description"]
    #         print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
    #             current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
# Loactions
    elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    # speak("User asked to Locate")
                    # speak(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
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
# Google search
    elif 'google' in query:
        query = query.replace("google", "")
        search_results = search(query, 10)
        return search_results
# Exit
    elif 'exit' in query or 'close' in query:
            speak("Thanks for giving me your time")
            exit()

    # elif "who i am" in query or 'who am i':
    #     return ("If you talk then definitely your human.")
    
    elif "why you came to world" in query:
            return ("Thanks to Jaswanth. further It's a secret")

    elif "will you be my girl friend" in query:
            return ("I'm not sure about, may be you should give me some time")
    
    elif "i love you" in query:
        return("Sorry I have a Boyfriend")

    elif "what's your name" in query or "What is your name" in query:
            return "Ny friends call me Giya"

    elif 'how are you' in query:
            return ("I am fine, Thank you! How are you, Sir")

    elif 'fine' in query or "good" in query:
            return("It's good to know that your fine")

    return None

def test(request):
    res = 'Give the command'
    if (request.method == "POST"):
        cmd = request.POST['cmd']
        
    return render(request,'testing.html',{'res':res,'cmd':cmd,})


