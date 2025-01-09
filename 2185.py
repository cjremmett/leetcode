from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if len(word) >= len(pref) and word[0:len(pref)] == pref:
                count += 1

        return count

if __name__ == '__main__':
    test_cases = ( [ ["pay","attention","practice","attend"], 'at', 2], [ ["leetcode","win","loops","success"], 'code', 0])
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' +str(case[2]) + '\nActual output: ' + str(Solution().prefixCount(case[0], case[1])) + '\n')