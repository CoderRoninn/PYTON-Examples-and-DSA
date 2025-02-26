class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
def main():
    first_node = ListNode(10)
    second_node = ListNode(20)
    third_node = ListNode(30)

    first_node.next = second_node
    first_node.prev = None

    second_node.next = third_node
    second_node.prev = first_node

    third_node.next = None
    third_node.prev = second_node

    temp = first_node

    while temp:
        print(temp.value, end="->")
        temp = temp.next
    print("NULL")    

if __name__ == "__main__":
    main()
