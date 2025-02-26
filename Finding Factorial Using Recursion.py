def calculate_factorial(x : int) -> int:
    if x == 0:   # for recursion there is edge case
        return 1
    
    return x * calculate_factorial(x-1)

def main():
    x = int(input("Enter a number:"))
    
    result = calculate_factorial(x)

    print(f"The result is:{result}")

if __name__ == "__main__":
    main()    
