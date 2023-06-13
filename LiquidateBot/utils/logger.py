import datetime

class Logger:
    def __init__(self):
        currenttime = datetime.datetime.now()
        self.filename = currenttime.strftime("%Y-%m-%d%H-%M-%S") + ".log"
        self.logfile = open(self.filename, "x")

    def log(self,content):
        fin = open(self.filename, "at")
        fin.write(content)
        fin.write("\n")
        fin.close()

loggerInstance = Logger()