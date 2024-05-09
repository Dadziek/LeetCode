class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)/2
        poss = list(set(nums))

        for i in poss:
            ammount = 0
            for j in nums:
                if i == j:
                    ammount += 1
            if ammount > size:
                return i
