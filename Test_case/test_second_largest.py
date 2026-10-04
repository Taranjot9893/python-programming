import sys
sys.path.append("code")

from second_largest import second_largest

assert second_largest([10, 20, 30, 40]) == 30
assert second_largest([5, 1, 9, 3]) == 5
assert second_largest([10, 10, 5, 2]) == 5
assert second_largest([100, 50, 75, 25]) == 75
assert second_largest([5]) == None

print("All test cases passed!")