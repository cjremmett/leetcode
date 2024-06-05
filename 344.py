from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        print(s)
        
if __name__ == '__main__':
    test_cases = ( (["h","e","l","l","o"], ["o","l","l","e","h"]), (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().reverseString(case[0])) + '\n')