class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
        else:
            for index, element in enumerate(nums):
                if target < element:
                    return index
            return len(nums)
