# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def calculate(first_value, second_value, third_value):
    result = 0

    if first_value > 0:
        result = result + first_value
    if second_value > 0:
        result = result + second_value
    if third_value > 0:
        result = result + third_value

    return result


def main():
    while True:
        first_value = ""
        first_value_is_int = isinstance(first_value, int)
        try:
            first_value = int(input("Choose first value : "))
            first_value_is_int = isinstance(first_value, int)
        except ValueError:
            print("Give number")
        if first_value_is_int:
            break

    while True:
        second_value = ""
        second_value_is_int = isinstance(second_value, int)
        try:
            second_value = int(input("Choose second value : "))
            second_value_is_int = isinstance(second_value, int)
        except ValueError:
            print("Give number")
        if second_value_is_int:
            break

    while True:
        third_value = ""
        third_value_is_int = isinstance(third_value, int)
        try:
            third_value = int(input("Choose third value : "))
            third_value_is_int = isinstance(third_value, int)
        except ValueError:
            print("Give number")
        if third_value_is_int:
            break

    print(calculate(first_value, second_value, third_value))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
