import asyncio
import os
import socket 
import threading

from modules.speech_to_text_bot import *

print('App starting')

if "PORT" in os.environ:
    socket = socket.socket().bind(('0.0.0.0', int(os.environ["PORT"]))).listen(1) # For heroku
    print('App bind port')

bot_config = {
    "api_token": os.environ["TELRGRAM_API_TOKEN"]
}

bot = SpeechToTextBot(bot_config)

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start_listening())