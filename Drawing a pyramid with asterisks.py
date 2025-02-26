def main():
    n = int(input("Enter a number"))

    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()    
if __name__ == "__main__":
    main() 