from datetime import datetime

class Applogger:
    def __init__(self) -> None:
        pass


    def log(self,log_file,log_message):
        self.now=datetime.now()
        self.date=self.now.date()
        self.current_time=self.now.strftime("%H:%M:%S")




        log_file.write(str(self.date)+"/"+str(self.current_time)+"\t\t"+log_message+'\n')

        



