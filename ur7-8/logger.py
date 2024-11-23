from fileinput import filename
from logging import FATAL, FileHandler, DEBUG, WARNING, warning, ERROR, error, CRITICAL, critical
from stat import filemode


class Logger:
    def __init__(self, fileName: str, level: int):
        self.fileName = fileName
        self.Level = level
    def __ConfigureLogger(self):
        format = Formatter('%(asctime)s : %(levelname)s - %(name)s - %(message)s')
        file_handler = FileHandler(filename=self.fileName, mode='a')
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)
    def __logDecorator(self, *exc_types):
        def Decorator(function):
            def Wrapper(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (exc_types) as ex:
                    raise ex
                return Wrapper
            return Decorator
        def __Log(self, message: str):
            if self.Level == DEBUG:
                self.__Logger.debug(message)
            elif self.Level == INFO:
                self.__Logger.debug(info)
            elif self.Level == WARNING:
                self.__Logger.debug(warning)
            elif self.Level == ERROR:
                self.__Logger.debug(error)
            elif self.Level == CRITICAL:
                self.__Logger.debug(critical)

        @__LogDecorator(Exception)
        def Log(self, message: str):
            try:
                self.__Log(message)
            except:
                 raise