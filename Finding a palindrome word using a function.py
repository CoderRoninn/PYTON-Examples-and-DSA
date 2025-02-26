def find_palindrome(my_string):
    length = len(my_string)
    i, j = 0, length -1

    while i < j:
        if my_string[i] != my_string[j]:
            return False
        i += 1
        j -= 1
    return True   

def main():

    my_string = input("Enter a word:")
    
    result = find_palindrome(my_string)

    if result:
        print("The word you entered is a palindrome word.")
    else:
        print("The word you entered isn't a palindrome word.")

if __name__ == "__main__":
    main()