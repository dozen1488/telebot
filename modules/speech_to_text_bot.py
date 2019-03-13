from .convert_ogg_module import convert
from .speech_recognition import recognize
from .bot_module import TelegramBot

class SpeechToTextBot(TelegramBot):
    def __init__(self, *params):
        TelegramBot.__init__(self, *params)
        self.update_callback = self.process_updates
    
    def process_message(self, message):
        try: 
            if message["message"]["voice"]:
                file_path = self.interactor.get_file_path(message["message"]["voice"]["file_id"])
                voice_content = self.interactor.get_voice_content(file_path)

                mp3_content = convert(voice_content)
                text = recognize(mp3_content)

                chat_id = message["message"]["chat"]["id"]
                self.interactor.send_message(chat_id, text)
        except:
            chat_id = message["message"]["chat"]["id"]
            text = 'Message should contain voice'

            self.interactor.send_message(chat_id, text)

    def process_updates(self, data):
        messages = data["result"]
        for message in messages:
            self.process_message(message)
