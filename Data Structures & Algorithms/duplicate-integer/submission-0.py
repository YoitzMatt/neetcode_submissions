class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Visited = {}
        for num in nums:
            if num in Visited:
                return True 
            else:
                Visited[num] = num 
        return False 