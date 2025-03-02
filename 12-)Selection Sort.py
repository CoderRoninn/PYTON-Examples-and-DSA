def selection_sort(my_list):
    length = len(my_list)

    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
def main():
    my_list = [14, 15, 19, 78, 36, 96, 49, 78]       
    print(f"Before sorting: {my_list}")        

    selection_sort(my_list)
    print(f"After sorting: {my_list}")
if __name__ == '__main__':
    main()  