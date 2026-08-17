class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l>=0 and r <n and s[l]==s[r]:
                l -=1
                r +=1
            return s[l+1:r]

        n = len(s)
        longest = ""
        for i in range(n):
            odd = expand(i,i)
            if (len(odd)>len(longest)):
                longest = odd
            even = expand(i,i+1)
            if (len(even)>len(longest)):
                longest = even
        return longest
