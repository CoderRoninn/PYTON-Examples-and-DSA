from collections import deque
from typing import Optional

class Queue:
    def __init__(self) -> None:
        self.elements = deque()  # it is more efficent then normal queue

    def is_empty(self) -> bool:
        return not self.elements

    def enqueue(self, element: int) -> None:
        self.elements.append(element)     #O(1)

    def dequeue(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements.popleft() # normaly it takes O(n) but in this method Takes O(1) it is faster then normal queue
        else:
            print("Queue is empty")
            return None
        
    def count(self) -> int:
        return len(self.elements)
    
    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements[0]
        else:
            print("The queue is empty. You can't peek")
            return None
def main():
    
    queue  = Queue()

    for element in [15, 25, 36, 98, 101]:
        queue.enqueue(element)        

    print(f"Queue count: {queue.count()}")    

    print(f"Peek: {queue.peek()}")

    removed_element = queue.dequeue()
    print(f"Dequeued: {removed_element} -> Queue: {queue.elements} ") 


if __name__ == "__main__":
    main()           