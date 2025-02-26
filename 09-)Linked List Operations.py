class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse(first_node):
    temp = first_node

    while temp:
        print(temp.value, end='->')
        temp = temp.next
    print("Null")      

def find_lowest_value(first_node):

    if not first_node:
        return None

    min_value = first_node.value
    temp = first_node.next

    while temp:
        if temp.value < min_value:
            min_value = temp.value
        temp = temp.next
    return min_value

def delete_node_front(first_node):
    if not first_node:
        print("There is no element to delete.")
        return None   
    first_node = first_node.next
    return first_node

def delete_node_specific(first_node, x):
    if not first_node:
        print("There is no element to delete")
        return None
    
    if first_node.value == x:
        first_node = first_node.next
        return first_node
    
    temp = first_node

    while temp.next and temp.next.value != x:
        temp = temp.next

    if not temp.next:
        print(f"Node with {x} not found.") 
        return first_node
    
    temp.next = temp.next.next   

    return first_node

def delete_node_end(first_node):
    if not first_node:
        print("There is no element to delete")
        return None
    
    if not first_node.next:
        return None
    
    temp = first_node

    while temp.next and temp.next.next:
        temp = temp.next

    temp.next = None

    return first_node    

def insert_node_atPosition(first_node, new_node, position):
    
    if not first_node:
        first_node = new_node
        return new_node
    
    if position == 1:
        new_node.next = first_node
        return new_node
    
    temp = first_node

    for _ in range(position -2):
        if not temp:
            print("Position is out of bounds.")
            return first_node
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node
    return first_node    

def main():

    first_node = ListNode(8)
    second_node =  ListNode(12)
    third_node = ListNode(6)
    fourth_node = ListNode(20)

    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = None

    print("Initial List:")
    traverse(first_node)

    print("\nList after deleting first node:")
    first_node = delete_node_front(first_node)
    traverse(first_node)

    print("\nList after deleting node with value 12:")
    first_node = delete_node_specific(first_node, 12)
    traverse(first_node)

    print("\nList after deleting last node:")
    first_node = delete_node_end(first_node)
    traverse(first_node)

    new_node = ListNode(15)
    print("\nList after inserting node 15 at position 2:")
    first_node = insert_node_atPosition(first_node, new_node, 2)
    traverse(first_node)

    print("\nThe lowest value in the list is:", find_lowest_value(first_node))

if __name__ == '__main__':
    main()
                