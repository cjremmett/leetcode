class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 10:
            return n * n
        
        n_without_zeros = 0
        
        multiplier = 1
        while 1 <= n:
            digit = n % 10
            n = n // 10
            if digit > 0:
                n_without_zeros += digit * multiplier
                multiplier *= 10

        n_sum = n_without_zeros
        sum_of_digits = 0
        while n_sum > 0:
            sum_of_digits += n_sum % 10
            n_sum = n_sum // 10

        return n_without_zeros * sum_of_digits
    

if __name__ == '__main__':
    test_cases = [(10203004, 12340), (100, 1)]
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected result: {case[1]}\nActual result: {Solution().sumAndMultiply(case[0])}\n')