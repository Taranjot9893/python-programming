import sys
sys.path.append("code")

from char_frequency import char_frequency

assert char_frequency("hello", "l") == 2
assert char_frequency("banana", "a") == 3
assert char_frequency("python", "p") == 1
assert char_frequency("apple", "z") == 0
assert char_frequency("aaaa", "a") == 4

print("All test cases passed!")