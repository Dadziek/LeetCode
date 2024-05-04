class Solution(object):
    def singleNumber(self, nums):
        for i in range(0, len(nums)):
            pair = False

            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i != j:
                    pair = True
                    break

            if pair is not True:
                return nums[i]
