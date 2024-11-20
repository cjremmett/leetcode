from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_customers_saved = 0
        max_cs_index = 0
        for i in range(0, len(customers) - minutes + 1):
            saved = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    saved += customers[j]
            
            if saved >= max_customers_saved:
                max_customers_saved = saved
                max_cs_index = i

        sum = 0
        for i in range(0, len(customers)):
            if grumpy[i] == 0:
                sum += customers[i]

        return sum + max_customers_saved

if __name__ == '__main__':
    test_cases = ( ([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3, 16), ([1], [0], 1, 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().maxSatisfied(case[0], case[1], case[2])) + '\n')