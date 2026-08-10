class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            area = height * abs(l - r)
            if area > m:
                m = area
            if height == heights[l]:
                l += 1
            else:
                r -= 1
        return m