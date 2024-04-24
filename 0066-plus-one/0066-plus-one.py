class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1]=1
            digits.append(0)
        return digits
        