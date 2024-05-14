from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0 or amount == 0 or coins[0] > amount:
            return -1

        if amount % coins[-1] == 0:
            return amount // coins[-1]
        else:
            segment_amount = amount % coins[-1]
            while segment_amount >= 0:
                result = self.check_segment
                
    def check_segment(self, coins, target, count):
        if len(coins) == 0 or coins[0] > target:
            return -1
        elif target % coins[-1] == 0:
            return count + target // coins[-1]
        else:
            result = self.check_segment(coins[:-1], target - coins[-1], count)
            if result == -1:
                return -1
            else:
                return count + result

        


if __name__ == '__main__':
    test_cases = ( ([3,5], 9, 3), ([1,2,5], 11, 3), ([2], 3, -1), ([1], 0, 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().coinChange(case[0], case[1])) + '\n')