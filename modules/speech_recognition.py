import speech_recognition as SR
import os
import sys
import webbrowser
import asyncio

from helpers import asyncronize_function

async def recognize(audio):
    r = SR.Recognizer()
    text = None
    try:
        audio_source = SR.AudioData(audio, 48000, 2)
        text = await asyncronize_function(
            r.recognize_google,
            audio_source,
            None,
            "ru-RU"
        )
    except SR.UnknownValueError:
        pass
    return text.lower() if text else text
