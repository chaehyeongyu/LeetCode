class Solution:
    def convert(self, s, numRows):
        rows = ['' for i in range(numRows)]
        left = s
        climb = False
        count = 0
        if numRows == 1:
            return s
        elif numRows == 2:
            r1 = ''
            r2 = ''
            for i in range(len(s)):
                if i%2:
                    r2 += s[i]
                else:
                    r1 += s[i]
            return r1 + r2
        while left != '':
            if climb == False:
                if count == (numRows - 1):
                    rows[count] += left[0]
                    left = left[1:]
                    climb = True
                    count = 0
                else:
                    rows[count] += left[0]
                    left = left[1:]
                    count += 1
            else:
                if count == (numRows - 3):
                    rows[numRows-2-count] += left[0]
                    left = left[1:]
                    climb = False
                    count = 0
                else:
                    rows[numRows-2-count] += left[0]
                    left = left[1:]
                    count +=1
        finalstr = ''
        for s in rows:
            finalstr += s
        return finalstr
