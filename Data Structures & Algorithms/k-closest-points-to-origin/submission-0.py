class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            d = math.sqrt(x**2 + y**2)
            heap.append([d,x,y])

        heapq.heapify(heap)
        
        res = []
        for _ in range(k):
            d,x,y = heapq.heappop(heap)
            res.append([x,y])

        return res
        