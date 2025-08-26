class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num_str = str(num)
            if len(num_str) == 1:
                return int(num_str)
            else:
                num_array = list(num_str)
                num_array = [int(x) for x in num_array]
                num = sum(num_array)


if __name__ == '__main__':
    test_cases = ( (38, 2), (0, 0))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected output: {case[1]}\nActual output: {Solution().addDigits(case[0])}\n')