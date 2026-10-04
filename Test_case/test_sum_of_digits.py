import sys
sys.path.append("code")

from sum_of_digits import sum_of_digits

assert sum_of_digits(12345) == 15
assert sum_of_digits(123) == 6
assert sum_of_digits(10) == 1
assert sum_of_digits(5) == 5
assert sum_of_digits(100) == 1

print("All test cases passed!")