from collections import defaultdict

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        indexes = defaultdict(list)
        for i in range(0, len(s)):
            indexes[s[i]].append(i)

        recent_pair = tuple()
        for i in range(0, len(t)):
            if len(recent_pair) == 0 and len(indexes[t[i]]) != 0:
                recent_pair = (t[i], indexes[t[i]][0])
            else:
                if t[i] in indexes:
                    for j in range(0, len(indexes[t[i]])):
                        if indexes[t[i]] > recent_pair[1]:
                            recent_pair = (t[i], indexes[t[i]][j])
                            break

                if len(recent_pair) > 0 and recent_pair[0] != t[i]:
                    return len(t[i:])

            return 0

if __name__ == '__main__':
    test_cases = ( ("coaching", "coding", 4), ("abcde", "a", 0), ("z", "abcde", 5))
    for case in test_cases:
        print('Input: ' + case[0] + ' ' + case[1] + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().appendCharacters(case[0], case[1])) + '\n')