import heapq
from typing import List, Optional

class MaxHeap:

    def __init__(self) -> None:
        self.heap = []

    def insert(self, value: int) -> None:
        heapq.heappush(self.heap, -value)  

    def remove(self) -> Optional[int]:
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)  

    def heapify(self) -> None:
        self.heap = [-x for x in self.heap]  
        heapq.heapify(self.heap)

    def get_max(self) -> Optional[int]:
        return -self.heap[0] if self.heap else None  

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def print_heap(self) -> None:
        print("Max heap:", [-x for x in self.heap])  