def is_valid(card_number):

    if len(card_number) != 16 or not card_number.isdigit():
        return False
    
    sum_even, sum_odd = 0, 0
    check = False

    for i in range(len(card_number)-1, -1, -1):
        number = int(card_number[i])
        if check:
            number = number *2
            if number > 9:
                number -= 9
            sum_even +=number
        else:
            sum_odd += number
        check = not check
    return (sum_odd + sum_even) % 10 == 0            


def main():
    card_number = input("Enter your card number:")

    if is_valid(card_number):
        print("Your card is valid.")
    else:
        print("Your card is invalid.")    


if __name__ == "__main__":
    main()    