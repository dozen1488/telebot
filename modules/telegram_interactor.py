import requests
import functools

from helpers import asyncronize_function
from errors.errors import GetFilePathError, GetVoiceContentError, GetUpdatesJsonError, SendMessageError, WebhookError

TELEGRAM_URL = "https://api.telegram.org"

class TelegramInteractor: 
    def __init__(self, api_token, hook_url=None, certificate_path=None):
        self.api_token = api_token
        self.hook_url = hook_url 
        self.certificate_path = certificate_path 

    async def get_file_path(self, file_id):
        try:
            params = {
                "file_id": file_id
            }
            response = await asyncronize_function(
                requests.get,
                TELEGRAM_URL + "/bot" + self.api_token + "/getFile",
                data=params
            )

            return response.json()["result"]["file_path"]
        except:
            raise GetFilePathError()

    async def get_voice_content(self, file_path):
        try: 
            response = await asyncronize_function(
                requests.get,
                TELEGRAM_URL + "/file/bot" + self.api_token + "/" + file_path
            )
            return response.content
        except:
            raise GetVoiceContentError()

    async def send_message(self, chat_id, message):
        try: 
            params = {
                "chat_id": chat_id,
                "text": message
            }
            response = await asyncronize_function(
                requests.get,
                TELEGRAM_URL + "/bot" + self.api_token + "/sendMessage",
                data=params
            )
            return response
        except:
            raise SendMessageError()

    async def get_updates_json(self, latest_update_id, timeout):
        try:
            params = {
                "timeout": timeout,
                "offset": latest_update_id + 1
            }
            response = await asyncronize_function(
                requests.get,
                TELEGRAM_URL + "/bot" + self.api_token + "/getUpdates",
                data=params
            )
            return response.json()
        except BaseException:
            raise GetUpdatesJsonError()

    async def create_webhook(self):
        try:
            if hasattr(self, 'hook_url') and hasattr(self, 'certificate_path'):
                with open(self.certificate_path) as certificate:
                    params = {
                        "url": self.hook_url,
                        "certificate": certificate
                    }
                    response = await asyncronize_function(
                        requests.post,
                        TELEGRAM_URL + "/bot" + self.api_token + "/setWebhook",
                        data=params
                    )
                    return response.json()
            else:
                return None
        except BaseException:
            raise WebhookError()

    async def delete_webhook(self):
        try:
            response = await asyncronize_function(
                requests.get,
                TELEGRAM_URL + "/bot" + self.api_token + "/deleteWebHook"
            )
            return response.json()
        except BaseException:
            raise WebhookError()
