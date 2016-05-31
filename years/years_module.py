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
    valami = years(age)
    #after = after_hundred_years
    print(name+" you will be 100 years old in: ", valami)
    return


if __name__ == '__main__':
    main()
