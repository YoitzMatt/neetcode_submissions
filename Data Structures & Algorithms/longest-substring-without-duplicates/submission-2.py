class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # intalize left and right pointers to 0
        # intalize a hashset and a return value to 0
        # WHILE right < len(s)
        # IF s[left:right] Do not contain repeats add s[right] to the hashset
        # Else increment left pointer and remove those characters from the set until there are no more
        # reapeating charecters

        res = l = 0
        seen = set()
        for r in range(len(s)):
            #seen.add(s[r])
            while s[r] in seen and l < len(s):
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            #print(f"seen: {seen}")
            res = max(res, len(seen))
        return res