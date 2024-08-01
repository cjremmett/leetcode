class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        num_full = numBottles
        num_empty = 0
        while num_full > 0 or num_empty >= numExchange:
            drunk += num_full
            new_num_full = (num_full + num_empty) // numExchange
            new_num_empty = (num_full + num_empty) % numExchange
            num_full, num_empty = new_num_full, new_num_empty

        return drunk       


if __name__ == '__main__':
    test_cases = ( (9, 3, 13), (15, 4, 19), (15, 8, 17))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' +str(case[2]) + '\nActual output: ' + str(Solution().numWaterBottles(case[0], case[1])) + '\n')