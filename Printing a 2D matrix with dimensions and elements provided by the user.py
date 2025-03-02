def main():

    rows, columns = map(int, input("Enter the dimensions of the 2-D array:").split())
    matrix = []

    for i in range(rows):
        row_elements = []
        for j in range(columns):
            element = int(input(f"Enter the element in {i+1}. row {j+1} column: "))
            row_elements.append(element)

        matrix.append(row_elements)

    print("Elements are: ")

    for row in matrix:
        print(" ".join(map(str,row)))

if __name__ == "__main__":
    main()
