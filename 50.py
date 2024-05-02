class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        negative = False
        
        if n < 0:
            negative = True
            n *= -1

        ri = x
        pointer = 0
        vals = [(1, x)]
        n -= 1
        while n > 0:
            if n >= vals[pointer][0] * 2:
                n -= vals[pointer][0] * 2 
                ri = ri * (vals[pointer][1] * vals[pointer][1])
                vals.append([vals[pointer][0] * 2, vals[pointer][1] * vals[pointer][1]])
                pointer += 1
            elif n >= vals[pointer][0]:
                n -= vals[pointer][0]
                ri = ri * (vals[pointer][1])
            else:
                pointer -= 1

        return ri if negative == False else 1 / ri
    
if __name__ == '__main__':
    test_cases = ( (2.00000, 10, 1024.00000), (2.10000, 3, 9.26100), (2.00000, -2, 0.25000), (0.00001, 2147483647, 0) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().myPow(case[0], case[1])) + '\n') 