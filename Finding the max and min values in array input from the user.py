def main():
    n = int(input("Enter the size of array"))

    x = []

    for i in range(n):
        element = int(input(f"Enter the {i+1}. element of array:"))
        x.append(element)

    max, min = max(x), min(x)

    print("The max value of array is:", max)
    print("The min value of array is: " ,min)
if __name__ == "__main__":
    main()    

