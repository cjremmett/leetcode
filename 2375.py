class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num_array = [str(i + 1) for i in range(0, len(pattern))]
        result = ''
        lp = 0
        rp = 0
        while True:
            if rp + 1 < len(pattern) and pattern[lp] == pattern[rp + 1]:
                rp += 1
                continue

            print("lp: " + str(lp) + ' rp: ' + str(rp))

            if pattern[lp] == 'I':
                result = result + ''.join(num_array[0:(rp - lp) + 1])
                num_array = num_array[(rp - lp) + 1:]
                lp = rp + 1
                rp += 1
            else:
                result = result + ''.join(reversed(num_array[0:(rp - lp) + 1]))
                num_array = num_array[(rp - lp) + 1:]
                lp = rp + 1
                rp += 1

            if len(num_array) == 0:
                break

        return result


if __name__ == '__main__':
    test_cases = [ ["IIIDIDDD", "123549876"], ["DDD", "4321"]]
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + case[1] + '\nActual output: ' + Solution().smallestNumber(case[0]) + '\n')
