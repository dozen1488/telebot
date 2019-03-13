import requests

TELEGRAM_URL = "https://api.telegram.org"

class TelegramInteractor: 
    def __init__(self, api_token):
        self.api_token = api_token

    def get_file_path(self, file_id):
        params = {
            "file_id": file_id
        }
        response = requests.get(TELEGRAM_URL + "/bot" + self.api_token + "/getFile", data=params)
        return response.json()["result"]["file_path"]

    def get_voice_content(self, file_path):
        response = requests.get(TELEGRAM_URL + "/file/bot" + self.api_token + "/" + file_path)
        return response.content

    def send_message(self, chat_id, message):
        params = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.get(TELEGRAM_URL + "/bot" + self.api_token + "/sendMessage", data=params)
        return response

    def get_updates_json(self, latest_update_id, timeout):
        params = {
            "timeout": timeout,
            "offset": latest_update_id + 1
        }
        response = requests.get(TELEGRAM_URL + "/bot" + self.api_token + "/getUpdates", data=params)
        return response.json()
    
class TelegramBot:
    def __init__(self, bot_config):
        self.interactor = TelegramInteractor(bot_config["api_token"])
        self.latest_update_id = 0
        self.update_callback = bot_config["update_callback"] if "update_callback" in bot_config else lambda *args: None
        self.listening = False
    
    def update_last_id(self, data):
        self.latest_update_id = data[-1]["update_id"] if data else self.latest_update_id

    def update_state(self):
        data = self.interactor.get_updates_json(self.latest_update_id, 5)
        if data["result"] and self.listening:
            self.update_last_id(data["result"])
            self.update_callback(data)
        if self.listening:
            self.update_state()

    def start_listening(self):
        self.listening = True
        self.update_state()

    def stop_listening(self):
        self.listening = False
