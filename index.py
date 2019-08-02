import asyncio
import os

from set_keep_alive_for_heroku import set_keep_alive_for_heroku, bind_port
from setup_for_aws_lambda import copy_ffmpeg_to_temp_folder

from modules.convert_ogg_module import get_converter_name
from modules.speech_to_text_bot import *

print('App starting')

bot_config = {
    "api_token": os.environ["TELRGRAM_API_TOKEN"]
}

converter_path = get_converter_name()

if "AWS_LAMBDA_FUNCTION_NAME" in os.environ:
    converter_path = copy_ffmpeg_to_temp_folder(os.environ["TEMP_FOLDER_NAME"])

bot = SpeechToTextBot(bot_config, converter_path)

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.update_state())