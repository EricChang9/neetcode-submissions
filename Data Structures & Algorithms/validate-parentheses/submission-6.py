class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comp = {"}" : "{",")" : "(", "]" : "["}

        for char in s:
            if char in comp:
                if stack and stack[-1] == comp[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack