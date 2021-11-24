# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def askuser():
    while True:
        user_value = ""
        user_value_is_int = isinstance(user_value, int)
        try:
            user_value = int(input("Choose a value : "))
            user_value_is_int = isinstance(user_value, int)
        except ValueError:
            print("Give number")
        if user_value_is_int:
            break
    return user_value


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
    first_value = askuser()
    second_value = askuser()
    third_value = askuser()

    print(calculate(first_value, second_value, third_value))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
