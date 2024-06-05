class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(1, len(s)):
            sum += abs(ord(s[i-1]) - ord(s[i]))

        return sum

if __name__ == '__main__':
    test_cases = ( ("hello", 13), ("zaz", 50))
    for case in test_cases:
        print('Input ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().scoreOfString(case[0])) + '\n')