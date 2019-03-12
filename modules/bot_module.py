import requests
from threading import Timer

TELEGRAM_URL = "https://api.telegram.org"

class Bot:
    def __init__(self, bot_config):
        self.api_token = bot_config["api_token"]
        self.latest_update_id = 0
        self.update_callback = bot_config["update_callback"]
        self.listening = False
    
    def get_updates_json(self):
        params = {
            "timeout": 5,
            "offset": self.latest_update_id + 1
        }
        response = requests.get(TELEGRAM_URL + "/bot" + self.api_token + "/getUpdates", data=params)
        return response.json()
    
    def update_last_id(self, data):
        self.latest_update_id = data[-1]["update_id"] if data else self.latest_update_id

    def update_state(self):
        data = self.get_updates_json()
        if data["result"] and self.listening:
            self.update_last_id(data["result"])
            self.update_callback(data)
        if self.listening:
            self.start_listening()

    def start_listening(self):
        self.timer = Timer(0, self.update_state)
        self.listening = True
        self.timer.start()

    def stop_listening(self):
        self.listening = False
        self.timer.cancel()

    def get_file_path(self, file_id):
        params = {
            "file_id": file_id
        }
        response = requests.get(TELEGRAM_URL + "/bot" + self.api_token + "/getFile", data=params)
        return response.json()["result"]["file_path"]

    def get_voice_content(self, file_path):
        response = requests.get(TELEGRAM_URL + "/file/bot" + self.api_token + "/" + file_path)
        return response.content