class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i,j):
            left = i
            right = j
            num_palindromes = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                    num_palindromes += 1
                else:
                    return num_palindromes
            return num_palindromes
            

        
        res = 0

        for i in range(len(s)-1):
            odd = expand(i, i)

            even = expand(i, i + 1)

            res += (odd + even)

        return res + 1
        