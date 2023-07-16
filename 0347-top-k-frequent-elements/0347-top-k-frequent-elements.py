from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        top_k = []
        while heap:
            top_k.append(heapq.heappop(heap)[1])

        return top_k[::-1] 