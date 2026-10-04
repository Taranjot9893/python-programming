def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[-2]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    result = second_largest(numbers)

    if result is None:
        print("Second largest number does not exist")
    else:
        print("Second largest number is:", result)