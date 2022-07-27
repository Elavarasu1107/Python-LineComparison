import math


def line_comparison(x1, y1, x2, y2):
    line_length = math.sqrt(math.pow(x2 - x1, 2) - math.pow(y2 - y1, 2))
    print("Line length: ", line_length)


if __name__ == '__main__':
    x1 = int(input("Enter value of X1: "))
    y1 = int(input("Enter value of Y1: "))
    x2 = int(input("Enter value of X2: "))
    y2 = int(input("Enter value of Y2: "))
    line_comparison(x1, y1, x2, y2)


