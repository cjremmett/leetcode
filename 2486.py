class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        indexes = {}
        for i in range(0, len(s)):
            if s[i] in indexes:
                indexes[s[i]].append(i)
            else:
                indexes[s[i]] = [i]

        recent_pair = tuple()
        for i in range(0, len(t)):
            if len(recent_pair) == 0 and t[i] in indexes:
                recent_pair = (t[i], indexes[t[i]][0])
            else:
                if t[i] in indexes:
                    for j in range(0, len(indexes[t[i]])):
                        if indexes[t[i]][j] > recent_pair[1]:
                            recent_pair = (t[i], indexes[t[i]][j])
                            indexes[t[i]] = indexes[t[i]][j+1:]
                            break
                else:
                    return len(t[i:])

        if len(recent_pair) > 0:
            return 0
        else:
            return len(t)

if __name__ == '__main__':
    test_cases = ( ("zbc", "abc", 3), ("coaching", "coding", 4), ("abcde", "a", 0), ("z", "abcde", 5))
    for case in test_cases:
        print('Input: ' + case[0] + ' ' + case[1] + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().appendCharacters(case[0], case[1])) + '\n')