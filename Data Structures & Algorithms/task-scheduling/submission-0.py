class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxn = max(count.values())
        maxcount = 0
        for k, v in count.items():
            if v == maxn:
                maxcount += 1
    
        option1 = (maxn - 1) * (n+1) + maxcount

        return max(option1, len(tasks))
        