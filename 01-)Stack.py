from typing import Optional

class Stack:
    def __init__(self) -> None:# for __init__ method we use
        self.stack = []        # the None type hint because it doesn't return any value
    
    def is_empty(self) -> bool:
        return self.stack == []
    
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.is_empty():
            self.stack.pop()
        else:
            print("The stack is empty. You can't do this operation")

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("There is no element to show")
            return None

    def count(self) -> int:
        return len(self.stack)
    
def main():
    my_stack = Stack()

    print(my_stack.is_empty())

    my_stack.push(200)
    my_stack.push(300)

    print(my_stack.peek())

    my_stack.pop()
    print(my_stack.peek())

if __name__ == "__main__":
    main()