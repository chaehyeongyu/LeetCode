class Solution:
    def longestCommonPrefix(self, strs):
        pre = ''
        for i in range(1,len(strs[0])+1):
            current_pre = strs[0][0:i]
            found = 0
            for s in strs:
                if current_pre == s[0:i]:
                    found += 1
            if found == len(strs) and len(current_pre) > len(pre):
                pre = current_pre
        return pre
