class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.log_file = open("logs.txt", "w")
        return cls.__instance

    def log(self, message):
        self.log_file.write(message + "\n")
        self.log_file.flush()


logger_one = Logger()
logger_one.log("Какого черта?")

logger_two = Logger()
logger_two.log("Да чтоб меня...!!!!!")

print(logger_one is logger_two)