class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        for n in hs:
            count = 0
            start = n
            if start - 1 in hs:
                continue

            while start in hs:
                count += 1
                start += 1
            
            res = max(res, count)
            
        return res