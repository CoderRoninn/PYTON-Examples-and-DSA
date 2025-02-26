from queue import LifoQueue

stack = LifoQueue()

stack.put(10) #This method adds a new element to the staeck
stack.put(20)
stack.put(30)

stack.get() #This medhod deletes element from the stack
stack.get()
stack.get()

from queue import Queue

queue = Queue()

queue.put(15) #This method adds a new element to the queue
queue.put(25)
queue.put(35)

queue.get()   #This medhod deletes element from the stack
queue.get()
queue.get()


from collections import deque

kdeque = deque()

kdeque.append(95) #This method adds a new element to the right of the deque
kdeque.append(85)

kdeque.appendleft(85) #This method adds a new element to the left of the deque

kdeque.pop() #This method deletes elements from the right of the deque
kdeque.popleft() #This method deletes elements from the left of the deque