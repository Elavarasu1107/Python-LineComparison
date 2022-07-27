import math


def line_comparison(x1, y1, x2, y2):
    """
    This function calculates length of a line
    :param x1: Coordinate x1 of a line
    :param y1: Coordinate y1 of a line
    :param x2: Coordinate x2 of a line
    :param y2: Coordinate y2 of a line
    :return: Length of a line
    """
    line_length = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    print("Line length: ", line_length)
    return line_length


if __name__ == '__main__':
    length = []
    for i in range(0, 2):
        x1 = int(input("Enter value of X1: "))
        y1 = int(input("Enter value of Y1: "))
        x2 = int(input("Enter value of X2: "))
        y2 = int(input("Enter value of Y2: "))
        length.append(line_comparison(x1, y1, x2, y2))
    if length[0] > length[1]:
        print("Line 1 is larger than Line 2")
    elif length[1] > length[0]:
        print("Line 2 is larger than Line 1")
    else:
        print("Both lines are Equal")


