class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(s) < len(part):
            return s

        lp = 0
        rp = len(part)

        while rp < len(s) + 1:
            if s[lp:rp] == part:
                s = s[0:lp] + s[rp:]
                lp -= len(part) - 1
                rp -= len(part) - 1
            else:
                lp += 1
                rp += 1

        return s


if __name__ == '__main__':
    test_cases = [ ["daabcbaabcbc", "abc", "dab"], ["axxxxyyyyb", "xy", "ab"] ]
    for case in test_cases:
        print('Input: ' + case[0] + ' ' + case[1] + '\nExpected output: ' + case[2] + '\nActual output: ' + Solution().removeOccurrences(case[0], case[1]) + '\n')
