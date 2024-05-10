class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title_chars = []
        while columnNumber:
            columnNumber -= 1
            title_chars.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(title_chars[::-1])