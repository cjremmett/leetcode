from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

    
    def can_meet_min(self, position, m, maxmin) -> bool:
        

if __name__ == '__main__':
    test_cases = ( ([1,2,3,4,7], 3, 3), ([5,4,3,2,1,1000000000], 2, 999999999))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().maxDistance(case[0], case[1])) + '\n')