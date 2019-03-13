class GetVoiceContentError(BaseException):
    def __init(self, *args):
        args[0] = "Error while getting file"
        BaseException(self, *args)