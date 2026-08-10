class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        ht = {}
        for i in range(len(s)):
            if s[i] not in hs:
                hs[s[i]] = 1
            elif s[i] in hs:
                hs[s[i]] += 1
            if t[i] not in ht:
                ht[t[i]] = 1
            elif s[i] in hs:
                ht[t[i]] += 1
        return hs == ht