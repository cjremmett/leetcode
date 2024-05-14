from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif len(coins) == 0:
            return -1

        values = set()
        values.update(coins)
        if amount in values:
            return 1
        i = 1
        while True:
            iteration_values = values.copy()
            i += 1
            if len(iteration_values) == 0:
                return -1
            for segment in iteration_values:
                for coin in coins:
                    if segment + coin == amount:
                        return i
                    elif segment + coin < amount:
                        values.add(segment + coin)
                values.discard(segment)

if __name__ == '__main__':
    test_cases = ( ([474,83,404,3], 264, 8), ([3,5], 9, 3), ([1,2,5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([1], 1, 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().coinChange(case[0], case[1])) + '\n')