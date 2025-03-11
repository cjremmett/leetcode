class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        return_count = 0
        counts = {'a': 0, 'b': 0, 'c': 0}
        counts[s[0]] += 1
        lp = 0
        rp = 0
        while True:
            if counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                lp += 1
                counts[s[lp]] -= 1
                return_count += len(s) - rp
            else:
                rp += 1
                if rp == len(s):
                    break
                counts[s[rp]] += 1

        return return_count


if __name__ == '__main__':
    test_cases = ( ("abcabc", 10), ("aaacb", 3), ("abc", 1))
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().numberOfSubstrings(case[0])) + '\n')
