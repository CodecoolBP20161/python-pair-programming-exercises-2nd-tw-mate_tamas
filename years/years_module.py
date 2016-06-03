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
    number = int(input("Type a number pls: "))
    years(age)
    after = years(age)
    print((name+", you will be 100 years old in: " + str(after)+" ")*number)
    for i in range(number):
        print(name+", you will be 100 years old in:", str(after) )


    return


if __name__ == '__main__':
    main()
