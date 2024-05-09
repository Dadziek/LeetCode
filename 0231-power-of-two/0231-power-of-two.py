class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        else:
            while n != 1:
                if n % 2 != 0:
                    return False
                n //= 2
            return True
