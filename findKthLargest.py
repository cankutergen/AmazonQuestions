from heapq import heapify, heappush, heappop


def findKthLargest(nums: List[int], k: int) -> int:
    minHeap = []
    heapify(minHeap)

    for i in nums:
        heappush(minHeap, i)

        if len(minHeap) > k:
            heappop(minHeap)

    return heappop(minHeap)
    
    
1 2 3 4 5
    
    
