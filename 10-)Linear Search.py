def linear_search(my_list, target):
    length = len(my_list)

    for i in range(length):
        if target == my_list[i]:
            return i
    return -1

def main():
    my_list = [11, 36, 96, 28, 97, 159, 257]
    target = int(input(f"Enter a number"))

    result = linear_search(my_list, target)

    if result == -1:
        print("The number you are looking for isn't in the list")    
    else:
        print(f"The number you are looking for is at index {result}") 
if __name__ =="__main__":
    main()                 
