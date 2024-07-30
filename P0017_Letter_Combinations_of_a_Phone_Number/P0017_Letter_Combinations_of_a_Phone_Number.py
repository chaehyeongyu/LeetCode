class Solution:
    def letterCombinations(self, digits):
        keypad=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        res = []

        # if len(digits) == 4:
        #     for l in keypad[int(digits[0])-2]:
        #         for m in keypad[int(digits[1])-2]:
        #             for n in keypad[int(digits[2])-2]:
        #                 for o in keypad[int(digits[3])-2]:
        #                     res.append(l+m+n+o)
        # elif len(digits) == 3:
        #     for l in keypad[int(digits[0])-2]:
        #         for m in keypad[int(digits[1])-2]:
        #             for n in keypad[int(digits[2])-2]:
        #                 res.append(l+m+n)
        # elif len(digits) == 2:
        #     for l in keypad[int(digits[0])-2]:
        #         for m in keypad[int(digits[1])-2]:
        #             res.append(l+m)
        # elif len(digits) == 1:
        #     for l in keypad[int(digits[0])-2]:
        #         res.append(l)
        # else:
        #     return []
        # return res
        if len(digits) == 0:
            return []
        res = [""]
        for digit in digits:
            new = []
            for c in res:
                for l in keypad[int(digit)-2]:
                    new.append(c + l)    
            res = new
        return res


        # if len(digits) == 0:
        #     return []
        # def rec(digits, curr):
        #     curr_res = []
        #     for i in curr:
        #         for j in keypad[int(digits[0])-2]:
        #             curr_res.append(i+j)
        #     if len(digits) == 1:
        #         return curr_res

        #     return rec(digits[1:], curr_res)


        # return rec(digits, [""])

