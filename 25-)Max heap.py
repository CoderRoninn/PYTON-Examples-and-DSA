from typing import Optional, List

class MaxHeap:

    def __init__(self) -> None:
        self.heap = []

    def insert(self, value: int) -> None:
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self.heap[i] > self.heap[(i-1) // 2]:
            self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2

    def remove_max(self) -> Optional[int]:
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0, len(self.heap))
        return root
    
    def max_heapify(self, i: int, n: int ) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:   
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest, n)     
    
    def built_heap(self, arr: List[int]) -> None:
        self.heap = arr[:]
        n = len(self.heap)
        
        for i in range((n//2)-1, -1, -1):
            self.max_heapify(i, n)

    def search(self, element: int) -> bool:
        for target in self.heap:
            if target == element:
                return True
        return False

    def getMax(self) -> Optional[int]:
        return self.heap[0] if self.heap else None

    def print_heap(self) -> None:
        print("Max heap:", *self.heap)        
        