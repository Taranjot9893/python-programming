def check_vowel_consonant(ch):
    if ch.lower() in "aeiou":
        return "Vowel"
    elif ch.isalpha():
        return "Consonant"
    else:
        return "Invalid"


if __name__ == "__main__":
    ch = input("Enter a character: ")
    print(check_vowel_consonant(ch))