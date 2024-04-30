class Solution:
    def reverseBits(self, n: int) -> int:
        out = ''
        quotient = n
        while quotient != 0:
            append = quotient % 2
            quotient = quotient // 2
            out = str(append) + out

        while len(out) < 32:
            out = '0' + out

        out = out[::-1]

        ret = 0
        for i in range(0, 32):
            ret += int(out[31 - i]) * (2**i)

        return ret
    

if __name__ == '__main__':
    test_cases = ( (43261596, 964176192), (1, 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().reverseBits(case[0])) + '\n')