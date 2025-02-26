class ListNode:
    def __init__(self, value):
        self.value =value
        self.next = None
def main():
    first_node = ListNode(10)
    second_node = ListNode(20)
    third_node = ListNode(30)

    first_node.next = second_node
    second_node.next = third_node        
    third_node.next = first_node

    temp = first_node
    

    while True:
        print(temp.value, end ="->")
        temp = temp.next
        if temp == first_node:
            break
    print("Head")  
if __name__ == "__main__":
    main()      
