class GetFilePathError(BaseException):
    def __init(self, *args):
        args[0] = "Error while getting file path"
        BaseException(self, *args)