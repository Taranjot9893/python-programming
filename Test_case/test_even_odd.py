def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
assert check_even_odd(10) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(0) == "Even"
print("All test cases passed")