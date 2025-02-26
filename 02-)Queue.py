from typing import Optional

class Queue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return self.elements == []
    
    def enqueue(self, element: int) -> None:    #insert element like push 
        self.elements.insert(0, element)

    def dequeue(self) -> Optional[int]:             #delete element
        if not self.is_empty():
            return self.elements.pop()
        else:
            print("The Queue is empty. You can't do this operation.")   
            return None 

    def count(self) -> int:
        return len(self.elements)
    
    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("The queue is empty. You can't peek.")
            return None
    
def main():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue count after enqueues:", queue.count())
    print("The element at the front of the queue is:", queue.peek())

    print("Dequeue element:", queue.dequeue())
    print("Queue count after first dequeue:", queue.count())

if __name__ == '__main__':
    main()



