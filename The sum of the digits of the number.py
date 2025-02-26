def main():
    number = int(input("Enter a number"))
    sum_digit = 0

    while number > 0:
        sum_digit += number % 10
        number // 10

    print(f"The sum of the digits of the number is: {sum_digit}")
if __name__ == "main":
    main() 