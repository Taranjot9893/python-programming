import sys
sys.path.append("code")

from vowels_consonants import check_vowel_consonant

assert check_vowel_consonant("a") == "Vowel"
assert check_vowel_consonant("E") == "Vowel"
assert check_vowel_consonant("b") == "Consonant"
assert check_vowel_consonant("Z") == "Consonant"
assert check_vowel_consonant("5") == "Invalid"

print("All test cases passed!")