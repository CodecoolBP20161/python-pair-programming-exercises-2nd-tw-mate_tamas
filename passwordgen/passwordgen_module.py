import random


def passwordgen():
    spec = ['!', '@', '#', '$', '%', '^', '&', ',', '*', '(', ')', '?']
    number = []
    upper = []
    lower = []
    password = []
    for i in range(65, 91):
        upper.append(chr(i))
    for i in range(97, 123):
        lower.append(chr(i))
    for i in range(48, 58):
        number.append(chr(i))
    password = random.sample(spec, 2) + random.sample(number, 2) + random.sample(upper, 2)+random.sample(lower, 2)
    password = ''.join(password)
    print(password)
    return password


def main():
    passwordgen()
    return

if __name__ == '__main__':
    main()
