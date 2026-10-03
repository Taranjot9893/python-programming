import sys
sys.path.append("code")
from pos_neg_zero import check_number
assert check_number(-8) == "Negative"
assert check_number(0) == "Zero"
assert check_number(5) == "Positive"
print("All test cases passed.")