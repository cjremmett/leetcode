from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num_consec = 0
        for num in arr:
            if num % 2 == 1:
                num_consec += 1
                if num_consec == 3:
                    return True
            else:
                num_consec = 0

        return False


if __name__ == '__main__':
    test_cases = ( ([2,6,4,1], False), ([1,2,34,3,4,5,7,23,12], True))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().threeConsecutiveOdds(case[0])) + '\n')