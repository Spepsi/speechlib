#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
import os

__all__ = ['get_voice', 'talk']
# obtain audio from the microphone
r = sr.Recognizer()

def get_voice(language="fr-FR"):
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    response = r.recognize_google(audio, language= language)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("you : " + response)
        return response
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def talk(sentence):
    blabla = (sentence)
    tts = gTTS(text=blabla, lang='fr')
    tts.save("sample.mp3")
    os.system("mpg321 sample.mp3")
    print("bot : "+str(sentence))
    return sentence

if __name__=='__main__':
    talk('coucou')
