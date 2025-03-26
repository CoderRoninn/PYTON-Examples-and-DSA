def main():

    n = int(input("Enter the size of array:"))

    x = []
    sum_elements  = 0

    for i in range(n):
        element = int(input(f"Enter the {i+1}. element of array: "))
        x.append(element)
        sum_elements += element
    average = sum_elements  / n

    print("The sum of array is: ", sum_elements )
    print("The average of array is: ", average)
if __name__ == "__main__":
    main()    

