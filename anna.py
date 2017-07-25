#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import wikipedia
import wolframalpha

app_id = "E82747-Y2LGY6EKH3"
client = wolframalpha.Client(app_id)


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data.lower():
        speak("I am fine")

    elif "anna wake up" in data.lower():
        speak("Welcome Sir!. What can i do for you")

    elif "what time is it" in data.lower():
        speak(ctime())

    # if "where is" in data:
    #     data = data.split(" ")
    #     location = data[2]
    #     speak("Hold on Sir, I will show you where " + location + " is.")
    #     os.system("firefox-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    elif "who is " in data.lower():
        data = data.split(" ")
        info = data[2]
        speak("Looking up your request sir!")
        query = wikipedia.summary(info, sentences=2)
        print(query)

    elif "exit" in data.lower():
        speak("Shutting down the system!")
        return 'break'

    else:
        try:
            speak("Looking up your request sir!")
            res = client.query(data)
            answer = next(res.results).text
            speak(answer)
        except:
            speak("No result found")
    time.sleep(2)


# initialization
time.sleep(2)
while True:
    data = recordAudio()
    if jarvis(data) == 'break':
        break
