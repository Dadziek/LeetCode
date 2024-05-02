class Solution(object):
    def findMaxK(self, nums):
        maxi = -1
        for i in nums:
            p = i * (-1)
            if p in nums:
                if i > 0 and maxi < i:
                    maxi = i
                else:
                    if maxi < p:
                        maxi = p
        return maxi
        