def char_frequency(text, char):
    return text.count(char)


if __name__ == "__main__":
    text = input("Enter a string: ")
    char = input("Enter a character: ")

    print("Frequency of character is:", char_frequency(text, char))