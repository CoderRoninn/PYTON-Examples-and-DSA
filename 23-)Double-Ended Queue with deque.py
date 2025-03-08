from collections import deque
from typing import Optional

class Queue:
    def __init__(self) -> None:
        self.elements = deque()  

    def is_empty(self) -> bool:
        return not self.elements  

    def add_left(self, element: int) -> None:
        self.elements.appendleft(element)  

    def add_right(self, element: int) -> None:
        self.elements.append(element) 

    def remove_left(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements.popleft()  
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
            return self.elements[0]  `
        else:
            print("The queue is empty.")
            return None

    def peek_right(self) -> Optional[int]:
        if not self.is_empty():
            return self.elements[-1]  
        else:
            print("The queue is empty.")
            return None      


