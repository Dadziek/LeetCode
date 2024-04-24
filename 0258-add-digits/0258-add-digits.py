class Solution(object):
    def addDigits(self, num):
        while True:
            num = sum(self.num2arr(num))
            if num < 10:
                return num

    def num2arr(self, num):
        arr = []
        while num:
            arr.append(num % 10)
            num //= 10
        return arr          
        