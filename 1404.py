class Solution:
    def numSteps(self, s: str) -> int:
        decimal_num = 0
        for i in range(0, len(s)):
            decimal_num += int(s[len(s) - 1 -  i]) * (2 ** i)

        i = 0
        while decimal_num != 1:
            i += 1
            if decimal_num % 2 == 0:
                decimal_num = decimal_num // 2
            else:
                decimal_num = decimal_num + 1

        return i

if __name__ == '__main__':
    test_cases = ( ("1111011110000011100000110001011011110010111001010111110001", 85), ("1101", 6), ("10", 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().numSteps(case[0])) + '\n')