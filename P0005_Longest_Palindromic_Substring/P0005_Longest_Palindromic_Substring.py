class Solution:
    def longestPalindrome(self, s):
        lp = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                piece = s[i:j]
                if piece == piece[::-1]:
                    if len(lp) < len(piece):
                        lp = piece
        return lp
