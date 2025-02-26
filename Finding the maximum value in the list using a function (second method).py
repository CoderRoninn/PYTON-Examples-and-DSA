def find_max(my_list):
    max_value = my_list[0]

    for i in range(1, len(my_list)):
        if max_value < my_list[i]:
            max_value = my_list[i]
    return max_value        
def main():
    my_list = [14, 19, 28, 39, 78]
    # We can easily find it without using a function or loop.   In this way  max_value = max(mylist)
    result = find_max(my_list)
    print(f"The max value in the list is: {result}")   
if __name__ == "__main__":
    main()             