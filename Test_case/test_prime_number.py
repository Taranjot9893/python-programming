import sys
sys.path.append("code")

from prime_number import check_prime

assert check_prime(2) == "prime"
assert check_prime(3) == "prime"
assert check_prime(7) == "prime"
assert check_prime(10) == "not prime"
assert check_prime(1) == "not prime"

print("All test cases passed!")