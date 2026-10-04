def fibonacci(n):
    series = []
    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    num = int(input("Enter the number of terms: "))
    print("Fibonacci series:", fibonacci(num))