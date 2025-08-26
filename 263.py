class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 7:
            return True
        elif n % 7 == 0:
            return False
        else:
            start = 11
            end = n // 2 + 2
            for i in range(start, end, 2):
                print(i)
                if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                    continue
                else:
                    if n % i == 0:
                        return False
                
            return True
        


if __name__ == '__main__':
    test_cases = ( (6, True), (1, True), (14, False), (22, False), (23, True))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected output: {case[1]}\nActual output: {Solution().isUgly(case[0])}\n')