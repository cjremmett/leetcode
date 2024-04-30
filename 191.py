class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        quotient = n
        while quotient != 0:
            remainder = quotient % 2
            quotient = quotient // 2
            if remainder == 1:
                count += 1

        return count
    
if __name__ == '__main__':
    test_cases = ( (11, 3), (128, 1) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().hammingWeight(case[0])) + '\n')