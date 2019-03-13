import requests
import subprocess
import sys

from threading import Timer
from modules.speech_to_text_bot import SpeechToTextBot
from modules.speech_recognition import recognize
from modules.convert_ogg_module import convert

bot_config = {
    "api_token": ""
}
bot = SpeechToTextBot(bot_config)

bot.start_listening()