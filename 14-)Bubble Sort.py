def bubble_sort(array):

    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j], array[j+1]


def main():

    array = [47, 19, 39, 28, 96]
    bubble_sort(array)
    print(array)
if __name__ =="__main__":
    main()
