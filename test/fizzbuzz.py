def fizzbuzz(n):
    result = ""
    if n % 3 == 0 or '3' in str(n):
        result += "Fizz"

    if n % 5 == 0 or '5' in str(n):
        result += "Buzz"
    return result if result else str(n)


if __name__ == "main":
    for i in range(1, 101):
        print(fizzbuzz(i))