import asyncio
import os
from set_keep_alive_for_heroku import set_keep_alive_for_heroku, bind_port

from modules.speech_to_text_bot import *

print('App starting')

bot_config = {
    "api_token": os.environ["TELRGRAM_API_TOKEN"]
}

bot = SpeechToTextBot(bot_config)

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start_listening())