def main():
    n = int(input("How many elements will there be: "))
    t1, t2 = 0, 1

    if n == 1:
        print(f"Fibonacci series: {t1}")
        print(f"The last element is: {t1}")

    if n == 2:
        print(f"Fibonacci series: {t1}, {t2}")
        print(f"The last element is: {t2}")

    else:
        print(f"Fibonacci series: {t1}, {t2}", end= ", ")
        for _ in range(2,n):
            next_number = t1 + t2
            print(next_number, end=", " if _ < n-2 else "")

            t1 = t2
            t2 = next_number
        print(f"The last element is: {next_number}")        
if __name__ == "__main__":
    main()  