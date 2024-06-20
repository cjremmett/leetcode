from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mapping = {}
        for i in range(0, len(capital)):
            if capital[i] in mapping:
                mapping[capital[i]].append(profits[i])
            else:
                mapping[capital[i]] == [profits[i]]

        capital.sort()

        profits = [0 for x in range(0, k)]


        pointer = 0
        for i in range(0, k):
            while capital[pointer] <= w:
                pointer += 1

    def binary_insert(profits, project, k):
        left_pointer = 0
        right_pointer = len(profits)
        while True:
            mid_pointer = (right_pointer - left_pointer) // 2
            if (mid_pointer - 1 < 0 or project >= profits[mid_pointer - 1]) and (mid_pointer >= len(profits) or project <= profits[mid_pointer]):
                profits.insert(mid_pointer, project)
                if len(profits) > k:
                    profits.pop(0)
                return
            elif (project >= profits[mid_pointer - 1]):
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1
            


if __name__ == '__main__':
    test_cases = ( (2, 0, [1,2,3], [0,1,1], 4), (3, 0, [1,2,3], [0,1,2], 6))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + ', ' + str(case[3]) + '\nExpected output: ' + str(case[4]) + '\nActual output: ' + str(Solution().findMaximizedCapital(case[0], case[1], case[2], case[3])) + '\n')