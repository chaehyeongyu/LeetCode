class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        roman = s[::-1]
        num = 0
        for i in range(len(roman)):
            if i > 0:
                if roman_dict[roman[i]] < roman_dict[roman[i-1]]:
                    num -= roman_dict[roman[i]]
                else:
                    num += roman_dict[roman[i]]
            else:
                num += roman_dict[roman[i]]
        return num
