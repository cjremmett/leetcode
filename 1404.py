class Solution:
    def numSteps(self, s: str) -> int:
        decimal_num = 0
        for i in range(0, len(s)):
            decimal_num += int(s[len(s) - 1 -  i]) * (2 ** i)

        return decimal_num

if __name__ == '__main__':
    test_cases = ( ("1101", 6), ("10", 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().numSteps(case[0])) + '\n')