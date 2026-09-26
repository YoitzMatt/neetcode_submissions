class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uc = set(s)
        res = 0
        for c in uc:
            l = 0
            k_count = 0
            for r in range(len(s)):
                if s[r] != c:
                    k_count += 1
                
                while k_count > k and l < len(s):
                    if s[l] != c:
                        k_count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res


