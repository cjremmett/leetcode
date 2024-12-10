from collections import defaultdict

class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return -1
        longest_length = 0
        sld = defaultdict(int)

        window = s[0]
        sld[window] += 1

        for i in range(1, len(s)):
            if window[-1] == s[i]:
                window += s[i]
            else:
                window = s[i]
            
            for i in range(0, 3):
                sld[window[:len(window) - i]] += 1
                if sld[window[:len(window) - i]] == 3:
                    if len(window[:len(window) - i]) > longest_length:
                        longest_length = len(window[:len(window) - i])
                if len(window) - i - 1 == 0:
                    break

        return longest_length if longest_length > 0 else -1


if __name__ == '__main__':
    test_cases = ( ["aaaa", 2], ["abcdef", -1], ["abcaba", 1])
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maximumLength(case[0])) + '\n')