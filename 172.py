import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        nfac = math.factorial(n)
        nfac = str(nfac)
        for i in reversed(range(0, len(nfac))):
            if nfac[i] == '0':
                count += 1
            else:
                return count

if __name__ == '__main__':
    test_cases = ( (3, 0), (5, 1), (0, 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().trailingZeroes(case[0])) + '\n')