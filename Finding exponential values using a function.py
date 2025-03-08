def calculate(x,y):
    result = 1
    for i in range(1,y+1):
        result *= x
    return result
    
def main():
    x,y = map(int, input("Enter the base and exponent: ").split())
    result = calculate(x,y)
    print(f"The result is: {result}")
if __name__ =="__main__":
    main()    


