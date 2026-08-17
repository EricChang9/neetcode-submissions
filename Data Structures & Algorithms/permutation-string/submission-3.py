class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            we wan to check all the len(s1) substrings in 2
            to check if its a permutation we can use set() because the set of 2 permutations
            are the same 
        """

        n = len(s1)

        if len(s2) < len(s1):
            return False 

        l, r = 0, n

        while r <= len(s2):
            curr = s2[l:r]
            print(Counter(s1), Counter(curr))
            if Counter(s1) == Counter(curr):
                return True
            print(l, r)
            l += 1
            r += 1

        return False