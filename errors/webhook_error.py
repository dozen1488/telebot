class WebhookError(BaseException):
    def __init(self, *args):
        args[0] = "Error acting with webhook"
        BaseException(self, *args)