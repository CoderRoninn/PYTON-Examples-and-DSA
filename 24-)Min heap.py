from typing import List, Optional

class MinHeap:

    def __init__(self) -> None: # Constructor to initialize a heap
        self.heap = []

    def insert(self, value: int) -> None: # it is a min heap and heapify-up
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self.heap[i] < self.heap[(i-1) // 2]:
            self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2

    def remove_min(self) -> Optional[int]: 
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0, len(self.heap))     # it is used to restore the min heap property after removing the smallest element       
        return root
    
    def min_heapify(self, i: int, n: int) -> None: # Heapify function to maintain the heap property and peapify-down
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < n and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest, n)

    def search(self, element: int) -> bool:
        for target in self.heap:
            if target == element:
                return True            
        return False
    
    def get_min(self) -> Optional[int]:
        return self.heap[0] if self.heap else None
    
    def print_heap(self) -> None:
        print("Min heap: ",*self.heap)

    def built_heap(self, arr: List[int]) -> None: # if there is existing list we can convert it to heap   
        self.heap = arr[:] #Make a copy to avoid changing the orginal list
        n = len(self.heap)  

        for i in range((n//2) - 1, -1, -1):
            self.min_heapify(i,n)

