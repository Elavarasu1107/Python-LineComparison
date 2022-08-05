import math
import logging

logging.basicConfig(filename='line_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Line:

    def __init__(self, details_dict):
        self.x1 = details_dict.get("x1")
        self.y1 = details_dict.get("y1")
        self.x2 = details_dict.get("x2")
        self.y2 = details_dict.get("y2")

    def length_finder(self):
        """
        This function calculates length of a line
        :return: Number
        """
        try:
            line_length = math.sqrt(math.pow(self.x2 - self.x1, 2) + math.pow(self.y2 - self.y1, 2))
            return line_length
        except Exception as ex:
            logger.exception(ex)

    def __eq__(self, line_obj):
        try:
            return self.length_finder() == line_obj.length_finder()
        except Exception as ex:
            logger.exception(ex)

    def __gt__(self, line_obj):
        try:
            return self.length_finder() > line_obj.length_finder()
        except Exception as ex:
            logger.exception(ex)

    def __lt__(self, line_obj):
        try:
            return self.length_finder() < line_obj.length_finder()
        except Exception as ex:
            logger.exception(ex)


def add_line():
    try:
        x1 = int(input("Enter value of X1: "))
        y1 = int(input("Enter value of Y1: "))
        x2 = int(input("Enter value of X2: "))
        y2 = int(input("Enter value of Y2: "))
        data_dict = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        line = Line(data_dict)
        return line
    except Exception as ex:
        logger.exception(ex)


if __name__ == '__main__':
    try:
        print("Enter data for line One: ")
        line_one = add_line()
        print("Enter data for line Two: ")
        line_two = add_line()

        if line_one > line_two:
            print("Line 1 is larger than Line 2 ")
        elif line_one < line_two:
            print("Line 2 is larger than Line 1 ")
        elif line_two == line_two:
            print("Both lines are equal")
    except Exception as e:
        logger.exception(e)
