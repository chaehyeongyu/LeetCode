class Solution:
    def threeSum(self, nums):
        ts = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i>= 1 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j<k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    new = [nums[i], nums[j], nums[k]]
                    ts.append(new)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                    while nums[k] == nums[k+1] and j<k:
                        k -= 1
        return ts
