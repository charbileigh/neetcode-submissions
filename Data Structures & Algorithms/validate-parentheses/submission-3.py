class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        if len(s) % 2 != 0:
            return False 

        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif (s[i] == ")" or s[i] == "]" or s[i] == "}") and len(stack) != 0:
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0