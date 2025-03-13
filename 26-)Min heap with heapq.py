import heapq
from typing import List, Optional

class MinHeap:

    def __init__(self) -> None:
        self.heap = []

    def insert(self, value: int) -> None:
        heapq.heappush(self.heap, value)

    def remove(self) -> Optional[int]:
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def heapify(self) -> None:
        heapq.heapify(self.heap)    