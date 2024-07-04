class Solution:
    def myAtoi(self, s: str) -> int:
        digits = '0123456789'
        left = s
        minus = False
        i = ''
        try:
            while left[0] == ' ':
                left = left[1:]
        except:
            pass
        try:
            if left[0] in '+-':
                minus = (left[0] == '-')
                left = left[1:]
        except:
            pass
        try:
            while left[0] == '0':
                left = left[1:]
        except:
            pass
        try:
            while left[0] in digits:
                i += left[0]
                left = left[1:]
        except:
            pass

    
        try:
            if minus:
                i = '-' + i
            i = int(i)
        except:
            return 0
        if i > 2**31 - 1:
            return 2**31 - 1
        elif i < -2**31:
            return -2**31
        else:
            return i
