from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        return []


if __name__ == '__main__':
    test_cases = ( ([5,4,3,2,1], [2,17,9,15,10], "RRRRR", [2,17,9,15,10]), ([3,5,2,6], [10,10,15,12], "RLRL", [14]), ([1,2,5,6], [10,10,11,11], "RLRL", []))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + case[2] + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().survivedRobotsHealths(case[0], case[1], case[2])) + '\n')