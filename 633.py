class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        dp_set = set()
        i = 0
        while True:
            new_square = i ** 2
            dp_set.add(new_square)
            if c - new_square in dp_set:
                return True
            elif new_square > c:
                return False
            else:
                i += 1
            

if __name__ == '__main__':
    test_cases = ( (5, True), (3, False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().judgeSquareSum(case[0])) + '\n')