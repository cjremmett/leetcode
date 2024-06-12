from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        num_out_of_order = 0
        for i in range(0, len(heights)):
            if heights[i] != sorted_heights[i]:
                num_out_of_order += 1

        return  num_out_of_order
    

if __name__ == '__main__':
    test_cases = ( ([1,1,4,2,1,3], 3), ([5,1,2,3,4], 5), ([1,2,3,4,5], 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().heightChecker(case[0])) + '\n')