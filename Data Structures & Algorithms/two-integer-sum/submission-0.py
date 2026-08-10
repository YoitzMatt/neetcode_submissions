class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Num_track = {}
        
        for i in range(len(nums)):
            diff =  target - nums[i]
            if diff in Num_track:
                return [Num_track[diff],i]
            Num_track[nums[i]] = i