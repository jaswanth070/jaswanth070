import speech_recognition as beta

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
