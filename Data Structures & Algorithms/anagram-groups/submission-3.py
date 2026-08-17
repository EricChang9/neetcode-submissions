class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        x = defaultdict(list)

        for str in strs:
            s = "".join(sorted(str))
            x[s].append(str)
        for v in x.values():
            res.append(v)

        return res
            