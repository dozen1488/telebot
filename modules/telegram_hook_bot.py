from .telegram_interactor import TelegramInteractor

class TelegramHookBot:
    def __init__(self, bot_config):
        self.interactor = TelegramInteractor(bot_config["api_token"])
        self.latest_update_id = 0
    
    def update_last_id(self, data):
        self.latest_update_id = data[-1]["update_id"] if data else self.latest_update_id

    async def update_state(self):
        data = await self.interactor.get_updates_json(self.latest_update_id, 0)
        if "result" in data:
            self.update_last_id(data["result"])
            await self.update_callback(data)
        await self.interactor.get_updates_json(self.latest_update_id, 0)
        

