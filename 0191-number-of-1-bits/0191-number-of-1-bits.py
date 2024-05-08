class Solution(object):
    def hammingWeight(self, n):
        ammount = 0
        binary = self.dec2bin(n)
        for i in binary:
            if i == "1":
                ammount += 1
        return ammount
    
    def dec2bin(self, n):
        binary = ""
        while n:
            binary += str(n%2)
            n //= 2
        return binary       