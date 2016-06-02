def palindrome(string_input):
    string_input = string_input.replace(" ", "").lower()
    print(string_input[0:] == string_input[::-1])
    return string_input[0:] == string_input[::-1]


def main():
    string_input = input("write a string:\n")
    palindrome(string_input)
    return

if __name__ == '__main__':
    main()
