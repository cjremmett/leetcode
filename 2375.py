class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num_array = [i for i in range(0, len(pattern))]
        result = ''
        lp = 0
        rp = 0
        while True:
            if rp + 1 < len(nums) and pattern[lp] == pattern[rp + 1]:
                rp += 1
                continue

            if pattern[lp] == 'I':
                result = result +




if __name__ == '__main__':
    test_cases = [ ["IIIDIDDD", "123549876"], ["DDD", "4321"]]
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + case[1] + '\nActual output: ' + Solution().smallestNumber(case[0]) + '\n')
