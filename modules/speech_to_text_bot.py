import asyncio
import time

from .convert_ogg_module import convert
from .speech_recognition import recognize
from .telegram_bot import TelegramBot

class SpeechToTextBot(TelegramBot):
    def __init__(self, *params):
        TelegramBot.__init__(self, *params)
        self.update_callback = self.process_updates
    
    async def process_message(self, message):
        try: 
            if message["message"]["voice"]:
                file_path = await self.interactor.get_file_path(message["message"]["voice"]["file_id"])
                voice_content = await self.interactor.get_voice_content(file_path)

                mp3_content = await convert(voice_content)
                text = await recognize(mp3_content)

                chat_id = message["message"]["chat"]["id"]
                await self.interactor.send_message(chat_id, text)
                print('Processed a message ' + str(time.time()))
        except BaseException as error:
            print(error)
            chat_id = message["message"]["chat"]["id"]
            text = 'Message should contain voice'

            await self.interactor.send_message(chat_id, text)

    def process_updates(self, data):
        messages = data["result"]
        if messages:
            print('Got a request ' + str(time.time()))
        for message in messages:
            asyncio.create_task(self.process_message(message))
