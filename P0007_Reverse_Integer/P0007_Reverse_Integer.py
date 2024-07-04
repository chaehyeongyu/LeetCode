class Solution:
    def reverse(self, x: int) -> int:
        num = ''
        s = str(x)
        minus = False
        if s[0] == '-':
            s = s[1:]
            minus = True
        s = s[::-1]
        while s != '':
            if num == '' and s[0] == '0':
                s = s[1:]
            else:
                num += s[0]
                s = s[1:]
        if minus:
            num = '-' + num
        if num == '':
            return 0
        elif int(num) > 2**31 - 1 or int(num) < - 2**31:
            return 0
        else:
            return int(num)
