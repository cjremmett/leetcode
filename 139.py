from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_size = max(map(len, wordDict))
        segment_indices = set()
        for i in range(0, len(s)):
            window = set()
            for j in range(1, max_size + 1):
                window.add(max(i-j, 0))
            
            for index in window:
                if index in segment_indices:
                    if s[index:i + 1] in wordDict:
                        segment_indices.add(i)
                        break
        
        if len(s) - 1 in segment_indices:
            return True
        else:
            return False

if __name__ == '__main__':
    test_cases = ( ('cars', ["car","ca","rs"], True), ("leetcode", {"leet","code"}, True), ("applepenapple", {"apple","pen"}, True), ("catsandog", {"cats","dog","sand","and","cat"}, False) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().wordBreak(case[0], case[1])) + '\n')