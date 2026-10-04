def reverse_string(text):
    return text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string is:", reverse_string(text))