from P0008_String_to_Integer_atoi import Solution

solution = Solution()
sol = solution.myAtoi('   -042')
print(sol)
sol = solution.myAtoi('1337c0d3')
print(sol)
sol = solution.myAtoi('0-1')
print(sol)
sol = solution.myAtoi('words and 987')
print(sol)
sol = solution.myAtoi('+-12')
print(sol)
