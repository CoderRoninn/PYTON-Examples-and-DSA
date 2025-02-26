class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
def main():
    first_node = ListNode(10)
    second_node = ListNode(20)
    third_node = ListNode(30)

    first_node.next = second_node
    second_node.next = third_node
    third_node.next = None # if we don't write this line pyton assigns third_node.next to None so it isn't required

    print(first_node.next.next.value)

    temp = first_node

    while temp:
        print(temp.value, end="->")
        temp = temp.next
    print("NULL")
if __name__ == "__main__":
    main()