def reverse_string(s):
    result = ""

    for char in s:
        result = char + result

    return result


if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Reversed string:", reverse_string(s))