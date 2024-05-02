from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        window = ''
        since_last = ''
        for i in range(0, len(s)):
            window += s[i]
            since_last += s[i]
            if window in wordDict:
                since_last = ''
            elif since_last in wordDict:
                if window not in wordDict:
                    window = since_last
                since_last = ''

        if len(since_last) > 0:
            return False
        else:
            return True

if __name__ == '__main__':
    test_cases = ( ('cars', ["car","ca","rs"], True), ("leetcode", {"leet","code"}, True), ("applepenapple", {"apple","pen"}, True), ("catsandog", {"cats","dog","sand","and","cat"}, False) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().wordBreak(case[0], case[1])) + '\n')