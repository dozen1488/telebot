class GetUpdatesJsonError(BaseException):
    def __init(self, *args):
        args[0] = "Error while updates"
        BaseException(self, *args)