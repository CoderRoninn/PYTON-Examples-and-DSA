from typing import Optional

class Queue: #  I will declare a linear queue
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return self.elements == []

    def enqueue(self, element: int) -> None:  #I used -> None to clearly indicate that this method does not return anything; it only modifies the queue."
        self.elements.append(element)  #o(1)

    def dequeue(self) -> Optional[int]: #I used Optional[int] for the return type because dequeue can either return an integer when successful or None when the queue is empty. 
        if not self.is_empty():
            return self.elements.pop(0) #o(n)
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
