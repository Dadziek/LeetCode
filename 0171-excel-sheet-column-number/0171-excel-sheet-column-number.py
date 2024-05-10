import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for c in columnTitle:
            ans = ans * 26 + ord(c) - ord('@')

        return ans