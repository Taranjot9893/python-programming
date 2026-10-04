def check_prime(num):
    if num < 2:
        return "not prime"

    for i in range(2, num):
        if num % i == 0:
            return "not prime"

    return "prime"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Number is", check_prime(num))