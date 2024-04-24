import string


class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        length = len(s)
        i = 1
        while True:
            if s[-i] not in string.ascii_letters:
                return i - 1
            i += 1
            if i > length:
                return i - 1
        