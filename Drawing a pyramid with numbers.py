def main():
    x = int(input("Enter a number:"))

    for i in range(x):
        for j in range(i+1):
            print(i+1, end="")
        print()    
if __name__ == "__main__":
    main()