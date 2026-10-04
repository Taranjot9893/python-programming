import sys
sys.path.append("code")

from reverse_number import reverse_number

assert reverse_number(12345) == 54321
assert reverse_number(123) == 321
assert reverse_number(10) == 1
assert reverse_number(5) == 5
assert reverse_number(100) == 1

print("All test cases passed!")