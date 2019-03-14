import asyncio
import os

from modules.speech_to_text_bot import *

bot_config = {
    "api_token": os.environ["TELRGRAM_API_TOKEN"]
}
bot = SpeechToTextBot(bot_config)

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start_listening())