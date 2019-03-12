import requests
import subprocess
import sys

from threading import Timer
from modules.bot_module import Bot
from modules.speech_recognition import recognize
from modules.convert_ogg_module import convert

def process_messages(data):
    messages = data["result"]
    for message in messages:
        if message["message"]["voice"]:
            file_path = bot.get_file_path(message["message"]["voice"]["file_id"])
            voice_content = bot.get_voice_content(file_path)
            mp3_content = convert(voice_content)
            text = recognize(mp3_content)
            print(text)

bot_config = {
    "api_token": "",
    "update_callback": process_messages
}
bot = Bot(bot_config)

bot.start_listening()
