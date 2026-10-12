class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anadic = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if anadic.get(s[i]):
                anadic[s[i]] += 1
            else:
                anadic.update({s[i]: 1})
        
        for j in range(len(t)):
            if anadic.get(t[j]):
                anadic[t[j]] -= 1
        
        sum = 0
        for k in anadic.values():
            sum += k

        if sum == 0:
            return True
        else:
            return False
