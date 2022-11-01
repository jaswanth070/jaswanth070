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
from voice_roc import takeCommand


def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]


def eval_binary_expr(op1, oper, op2):
     op1,op2 = int(op1), int(op2)
     return get_operator_fn(oper)(op1, op2)

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
    speak(assname)

def clear(): return os.system('cls')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(eval_binary_expr(*(my_string.split())))
if __name__ == '__main__':
    clear()
    wishMe()

    while True:
        try:
            query = takeCommand().lower()

            if not query is None:
                print(query)
# Youtube
                if 'open youtube' in query or 'open YouTube' in query:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("youtube.com")
                    os.system('cls')
# Wikipedia
                elif 'wikipedia' in query or 'Wikipedia' in query :
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    os.system('cls')
# Google
                elif 'open google' in query:
                        speak("Here you go to Google\n")
                        webbrowser.open("google.com")
                        os.system('cls')
# Stack Overflow
                elif 'open stackoverflow' in query:
                    speak("Here you go to Stack Over flow.Happy coding")
                    webbrowser.open("stackoverflow.com")
                    os.system('cls')
# Instagram
                elif 'open instagram' in query:
                    speak("Here you go to Instagram")
                    webbrowser.open("instagram.com")
                    os.system('cls')
# Jokes  
                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)
                    os.system('cls')
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
                
                elif "weather" in query:
                    # Google Open weather website
                    # to get API of Open weather
                    api_key = "Api key"
                    base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                    speak(" City name ")
                    print("City name : ")
                    city_name = takeCommand()
                    complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                    response = request.get(complete_url)
                    x = response.json()

                    if x["code"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_pressure = y["pressure"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
                            current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

                elif 'search' in query or 'play' in query:
                    query = query.replace("search", "")
                    query = query.replace("play", "")
                    webbrowser.open(query)

                elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                        print(strTime)
                        speak(f"Sir, the time is {strTime}")
                        print('\n')

                elif 'who is your boyfriend' in query:
                    speak('Surendhar from CME 2')

                elif 'how are you' in query:
                        speak("I am fine, Thank you")
                        speak("How are you, Sir")
                        print('\n')

                elif 'fine' in query or "good" in query:
                        speak("It's good to know that your fine")
                        print('\n')

                elif "what's your name" in query or "What is your name" in query:
                        speak("My friends call me")
                        speak("Giya")
                        print("My friends call me Giya")
                        print('\n')

                elif 'exit' in query or 'close' in query:
                        speak("Thanks for giving me your time")
                        exit()

                elif "calculate" in query:

                    app_id = "U946LA-262EX4V97V"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('calculate')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)
                    print('\n')

                elif 'what' in query:
                    app_id = "U946LA-262EX4V97V"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('what')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)
                    print('\n')

                elif 'who' in query:
                    app_id = "U946LA-262EX4V97V"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('who')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)
                    print('\n')

                elif 'where' in query:
                    app_id = "U946LA-262EX4V97V"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('where')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)
                    print('\n')

                elif 'when' in query:
                    app_id = "U946LA-262EX4V97V"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('when')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    print('\n')

                elif 'why' in query:
                    app_id = "U946LA-262EX4V97V"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('how')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    print('\n')
                
                elif 'search' in query or 'play' in query:
                    query = query.replace("search", "")
                    query = query.replace("play", "")
                    webbrowser.open(query)
                
                elif "who i am" in query:
                    speak("If you talk then definitely your human.")
                
                elif "will you be my girl friend" in query:
                    speak("I'm not sure about, may be you should give me some time")

                elif "why you came to world" in query:
                    speak("Thanks to Jaswanth. further It's a secret")
                
                elif "i love you" in query:
                    speak("Sorry I have a Boyfriend")
                
                elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
                elif "created you" in query or "who made you" in query:
                    print("Thanks to Jaswanth, for bringing me to this world")
                    print("Thanks to Jaswanth, for bringing me to this world")
                                        
        except:
            speak('Something went wrong')
            speak('Please Try Again')
            print('Something went wrong')
