import datetime
from datetime import date


def years(age):
    n = 100 - age
    after_hundred_years = date.today().year+n
    after = after_hundred_years
    return after


def main():
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    years(age)
    after = years(age)
    print(name+" you will be 100 years old in: ", after)  # I can use just print without defining after
    return


if __name__ == '__main__':
    main()
