import logging
import logging_employee


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("sample.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging.basicConfig(filename="sample.log", level=logging.DEBUG,
#                    format="%(asctime)s:%(name)s:%(message)s")


def sum(x, y):
    return x+y


def substract(x, y):
    return x-y


num_1 = 10
num_2 = 5

result_sum = sum(num_1, num_2)
logger.debug("Add: {} + {} = {}".format(num_1, num_2, result_sum))

result_sub = substract(num_1, num_2)
logger.debug("Substract: {} - {} = {}".format(num_1, num_2, result_sub))
