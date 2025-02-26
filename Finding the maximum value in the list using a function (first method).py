def find_max(array):
    max_value = array[0]

    for number in array[1:]:
        if number > max_value:
            max_value = number
    return max_value
def main():
    my_list = [17, 28, 39 ,49]        
    result = find_max(my_list) # We can easily find it without using a function or loop.   In this way  max_value = max(mylist)


    print(f"The max value in the list is: {result}")
if __name__ == '__main__':
    main()   