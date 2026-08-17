class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = Counter(s)
        t2 = Counter(t)

        return s2 == t2