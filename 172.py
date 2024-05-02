import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        nfac = math.factorial(n)
        while True:
            if nfac % 10 == 0:
                count += 1
                nfac = nfac // 10
            else:
                return count
            

if __name__ == '__main__':
    num = 1234
    first_digit = num 
    test_cases = ( (3, 0), (5, 1), (0, 0), (4830, 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().trailingZeroes(case[0])) + '\n')