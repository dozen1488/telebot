import requests
import asyncio
import functools

from errors.errors import GetFilePathError, GetVoiceContentError, GetUpdatesJsonError, SendMessageError

TELEGRAM_URL = "https://api.telegram.org"

class TelegramInteractor: 
    def __init__(self, api_token):
        self.api_token = api_token
        self.loop = asyncio.get_event_loop()

    async def get_file_path(self, file_id):
        try:
            params = {
                "file_id": file_id
            }
            response = await self.loop.run_in_executor(None, functools.partial(requests.get, TELEGRAM_URL + "/bot" + self.api_token + "/getFile", data=params))

            return response.json()["result"]["file_path"]
        except:
            raise GetFilePathError()

    async def get_voice_content(self, file_path):
        try: 
            response = await self.loop.run_in_executor(None, functools.partial(requests.get, TELEGRAM_URL + "/file/bot" + self.api_token + "/" + file_path))
            return response.content
        except:
            raise GetVoiceContentError()

    async def send_message(self, chat_id, message):
        try: 
            params = {
                "chat_id": chat_id,
                "text": message
            }
            response = await self.loop.run_in_executor(None, functools.partial(requests.get, TELEGRAM_URL + "/bot" + self.api_token + "/sendMessage", data=params))
            return response
        except:
            raise SendMessageError()

    async def get_updates_json(self, latest_update_id, timeout):
        try:
            params = {
                "timeout": timeout,
                "offset": latest_update_id + 1
            }
            response = await self.loop.run_in_executor(None, functools.partial(requests.get, TELEGRAM_URL + "/bot" + self.api_token + "/getUpdates", data=params))
            return response.json()
        except BaseException:
            raise GetUpdatesJsonError()
