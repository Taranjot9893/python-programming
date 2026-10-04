import sys
sys.path.append("code")

from palindrome_string import is_palindrome_string

assert is_palindrome_string("madam") == True
assert is_palindrome_string("level") == True
assert is_palindrome_string("racecar") == True
assert is_palindrome_string("hello") == False
assert is_palindrome_string("python") == False

print("All test cases passed!")