def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
assert largest_of_three(10, 20, 30) == 30
assert largest_of_three(50, 20, 10) == 50
assert largest_of_three(10, 40, 20) == 40
assert largest_of_three(5, 5, 2) == 5
print("All test cases passed")