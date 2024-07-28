class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        curr = 10**4+3*1000+1
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j<k:
                currsum = nums[i] + nums[j] + nums[k]
                if currsum > target:
                    new = currsum - target
                    if new < curr:
                        curr = new
                        res = currsum
                    k -= 1
                elif currsum < target:
                    new = target - currsum
                    if new < curr:
                        curr = new
                        res = currsum
                    j += 1
                else:
                    return target
        return res
