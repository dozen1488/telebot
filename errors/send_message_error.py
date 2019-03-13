class SendMessageError(BaseException):
    def __init(self, *args):
        args[0] = "Error while sending message"
        BaseException(self, *args)