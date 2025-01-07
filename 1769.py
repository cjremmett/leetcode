from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        return []

if __name__ == '__main__':
    test_cases = [ ["110", [1,1,3]], ["001011", [11,8,5,4,3,4]]]
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minOperations(case[0])) + '\n')