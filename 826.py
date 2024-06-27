from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        highest_possible_profit = 0
        result = 0
        mapping = [(difficulty[i], profit[i]) for i in range(0, len(profit))]
        mapping.sort(key=lambda x: x[0])
        worker.sort()
        
        pointer = 0
        for work in worker:
            while pointer < len(mapping) and work >= mapping[pointer][0]:
                if mapping[pointer][1] > highest_possible_profit:
                    highest_possible_profit = mapping[pointer][1]
                pointer += 1

            result += highest_possible_profit

        return result

        
if __name__ == '__main__':
    test_cases = ( ([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7], 100), ([85,47,57], [24,66,99], [40,25,25], 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + ' ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().maxProfitAssignment(case[0], case[1], case[2])) + '\n')