import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_Handler = logging.FileHandler("employee.log")
file_Handler.setFormatter(formatter)

logger.addHandler(file_Handler)

#logging.basicConfig(filename="employee.log",level=logging.INFO,format="%(levelname)s:%(name)s:%(message)s")

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("Created employee: {} - {}".format(self.fullname, self.email))
    
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

Employee("Benjamin", "Nass")