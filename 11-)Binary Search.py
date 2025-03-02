def binary_search(my_list, target):
    left, right = 0, len(my_list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if my_list[mid] == target:
            return mid
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def main():
    my_list = [105, 109, 110, 259, 369, 789, 859]     
    x = int(input("Enter a number")) 

    result = binary_search(my_list, x)

    if result == -1:
        print("The element you are looking for isn't in the list")  
    else:
        print(f"The element you are looking for at index {result}")    
if __name__ == "__main__":
    main() 