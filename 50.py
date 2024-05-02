class Solution:
    def myPow(self, x: float, n: int) -> float:
        return 0.0
    
if __name__ == '__main__':
    test_cases = ( (2.00000, 10, 1024.00000), (2.10000, 3, 9.26100), (2.00000, -2, 0.25000) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().myPow(case[0], case[1])) + '\n') 