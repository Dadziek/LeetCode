class Solution(object):
    def plusOne(self, digits):
        for i in range(-1, -len(digits)-1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            else:
                digits[i] = 0

        digits.insert(0, 1)
        return digits
