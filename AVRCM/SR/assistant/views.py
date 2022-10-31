from django.shortcuts import render,HttpResponse,redirect
import datetime
import operator
import os
import webbrowser
import wikipedia
import wolframalpha
import pyttsx3


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


def test(request):
    res = 'Give the command'
    if (request.method == "POST"):
        cmd = request.POST['cmd']
    return render(request,'testing.html',{'res':res})


