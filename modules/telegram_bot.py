from .telegram_interactor import TelegramInteractor

class TelegramBot:
    def __init__(self, bot_config):
        self.interactor = TelegramInteractor(bot_config["api_token"])
        self.latest_update_id = 0
        self.update_callback = bot_config["update_callback"] if "update_callback" in bot_config else lambda *args: None
        self.listening = False
    
    def update_last_id(self, data):
        self.latest_update_id = data[-1]["update_id"] if data else self.latest_update_id

    async def update_state(self):
        data = await self.interactor.get_updates_json(self.latest_update_id, 20)
        if "result" in data and self.listening:
            self.update_last_id(data["result"])
            self.update_callback(data)

    async def listen(self):
        while self.listening:
            await self.update_state()

    async def start_listening(self):
        self.listening = True
        await self.listen()

    def stop_listening(self):
        self.listening = False
