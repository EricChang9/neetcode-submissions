class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = dict()
        set_t = dict()
        for char in s:
            if char in set_s.keys():
                set_s[char] += 1
            else:
                set_s[char] = 1
        for char in t:
            if char in set_t.keys():
                set_t[char] += 1
            else:
                set_t[char] = 1
        return set_s == set_t