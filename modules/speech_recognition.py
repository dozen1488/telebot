import speech_recognition as SR
import os
import sys
import webbrowser

def recognize(audio):
    r = SR.Recognizer()
    text = None
    try:
        audio_source = SR.AudioData(audio, 48000, 2)
        text = r.recognize_google(audio_source, None, "ru-RU").lower()
    except SR.UnknownValueError:
        pass
    return text
