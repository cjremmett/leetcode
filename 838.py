class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) == 0:
            return ''
        
        dominoes = [dominoes[i] for i in range(0, len(dominoes))]
        lp = 0
        rp = 0
        while lp < len(dominoes):
            if dominoes[lp] != '.':
                lp += 1
            else:
                rp = lp + 1
                while rp < len(dominoes) and dominoes[rp] == '.':
                    rp += 1
                
                self.process_window(dominoes, lp, rp)
                lp = rp

        return ''.join(dominoes)
        
                
    def process_window(self, dominoes, lp, rp):
        if lp - 1 < 0 and rp == len(dominoes):
            pass
        elif lp - 1 < 0 and rp < len(dominoes):
            if dominoes[rp] == 'L':
                for i in range(lp, rp):
                    dominoes[i] = 'L'
        elif lp - 1 >= 0 and rp == len(dominoes):
            if dominoes[lp-1] == 'R':
                for i in range(lp, rp):
                    dominoes[i] = 'R'
        else:
            if dominoes[lp - 1] == dominoes[rp]:
                for i in range(lp, rp):
                    dominoes[i] = dominoes[lp - 1]
            elif dominoes[lp - 1] == 'R':
                half = (rp - lp) // 2
                for i in range(lp, lp + half):
                    dominoes[i] = 'R'
                m = (rp - lp) % 2
                for i in range(lp+half+m, rp):
                    dominoes[i] = 'L'
        

if __name__ == '__main__':
    test_cases = ( ("RR.L", "RR.L"), (".L.R...LR..L..", "LL.RR.LLRRLL.."), (".L.R.", "LL.RR") )
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + case[1] + '\nActual output: ' + Solution().pushDominoes(case[0]) + '\n') 