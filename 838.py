class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) == 0:
            return ''
        
        

if __name__ == '__main__':
    test_cases = ( ("RR.L", "RR.L"), (".L.R...LR..L..", "LL.RR.LLRRLL..") )
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + case[1] + '\nActual output: ' + Solution().pushDominoes(case[0]) + '\n') 