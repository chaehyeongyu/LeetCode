class Solution:
    def maxArea(self, height):
        curr = 0
        left = 0
        minh = 0
        right = len(height) - 1
        while left < right:
            base = right - left
            if height[left] <= height[right]:
                minh = height[left]
                if base * minh >= curr:
                    curr = base * minh
                left += 1
            else:
                minh = height[right]
                if base * minh >= curr:
                    curr = base * minh
                right -= 1
        return curr
