class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lenlss = 0
        # for i in range(1, len(s)+1):
        #     for j in range(len(s)-i+1):
        #         if len(s[j:j+i]) == len(set(s[j:j+i])) and len(s[j:j+i]) > lenlss:
        #             lenlss = len(s[j:j+i])
        # return lenlss
        lenlss = 0
        curr_ss=''
        for i in range(len(s)):
            if s[i] not in curr_ss:
                curr_ss += s[i]
            else:
                ss1, ss2 = curr_ss.split(s[i])
                curr_ss = ss2 + s[i]
            if len(curr_ss) > lenlss:
                lenlss = len(curr_ss)
        return lenlss
