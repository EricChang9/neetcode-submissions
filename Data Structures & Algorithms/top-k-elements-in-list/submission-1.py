class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        elems = []
        for i, (key,v) in enumerate(count.items()):
            elems.append(((v,key)))
        for el in elems:
            heapq.heappush(heap, el)
            print(len(heap) > k)
            print(len(heap))
            print(k)
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)
        res = [x[1] for x in heap]
        return res
            