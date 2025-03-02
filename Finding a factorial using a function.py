    def main():

        x = int(input("Enter a number: "))
        result = 1

        for i in range(1, x+1):
            result *= i

        print(f"The result is {result}")
    if __name__ == "__main__":
        main()       