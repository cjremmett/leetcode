class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return_to_start = (n - 1) * 2
        real_movement = time % return_to_start
        if real_movement <= n - 1:
            return 1 + real_movement
        else:
            return n - (real_movement - (n - 1))


if __name__ == '__main__':
    test_cases = ( (4, 5, 2), (3, 2, 3))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().passThePillow(case[0], case[1])) + '\n')