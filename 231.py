class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1 and n % 2 == 0:
            n = n // 2
        
        return False if n > 1 else True


if __name__ == '__main__':
    test_cases = ( (1, True), (16, True), (3, False))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected output: {case[1]}\nActual output: {Solution().isPowerOfTwo(case[0])}\n')