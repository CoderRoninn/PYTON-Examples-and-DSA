from typing import Optional

class Queue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return self.elements == []

    def add_left(self, element: int) -> None:
        self.elements.insert(0, element) #O(N)
 
    def add_right(self, element: int) -> None:
        self.elements.append(element) #O(1)

    def remove_left(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements.pop(0) #o(N)
        else:
            print("The queue is empty.")
            return None
    def remove_right(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements.pop()
        else:
            print("The queue is empty.")
            return None
        
    def count(self) -> int:
        return len(self.elements)
    
    def peek_left(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements[0]
        else:
            print("The queue is empty.")
            return None

    def peek_right(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("The queue is empty.")
            return None
        
def main():

    queue = Queue()

    queue.add_right(10)
    queue.add_right(20)
    queue.add_right(30)
    print(f"After adding from right operation {queue.elements}")

    queue.add_left(5)
    queue.add_left(1)
    print(f"After adding from left operation {queue.elements}")

    print(f"Peek Left: {queue.peek_left()}")
    print(f"Peek Right: {queue.peek_right()}")

    
    print(f"Peek Left: {queue.peek_left()}")
    print(f"Peek Right: {queue.peek_right()}")

    
    removed_left = queue.remove_left()
    print(f"Removed from left: {removed_left}, Updated Queue: {queue.elements}")

    
    removed_right = queue.remove_right()
    print(f"Removed from right: {removed_right}, Updated Queue: {queue.elements}")

    
    print(f"Queue size: {queue.count()}")
if __name__ =="__main__":
    main()    

            






