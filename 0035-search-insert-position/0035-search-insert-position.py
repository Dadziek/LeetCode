class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            left = 0
            right = len(nums) - 1
            mid = (left + right) // 2

            while left <= right:
                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = mid
                    mid = (left + right) // 2
                
                else:
                    right = mid
                    mid = (left + right) // 2
        else:
            for index, element in enumerate(nums):
                if target < element:
                    return index
            return len(nums)
