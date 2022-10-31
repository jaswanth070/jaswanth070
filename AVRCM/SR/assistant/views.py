from django.shortcuts import render,HttpResponse,redirect
import datetime
import operator
import os
import webbrowser
import wikipedia
import wolframalpha
import pyttsx3
import speech_recognition as beta


# Create your views here.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def home(request):
    return HttpResponse('This is the main page!')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def assistant(request):
    return render(request,'base.html')

def takeCommand():
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


def test(request):
    res = 'Give the command'
    if (request.method == "POST"):
        cmd = request.POST['cmd']
    return render(request,'testing.html',{'res':res})


