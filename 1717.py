class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        count = 0
        index = 0
        if x > y:
            larger_op = 'ab'
            smaller_op = 'ba'
        else:
            larger_op = 'ba'
            smaller_op = 'ab'
        
        loa = max(x, y)
        soa = min(x, y)
        
        while index <= len(s) - 2:
            if s[index:index+2] == larger_op:
                count += loa
                s = s[:index] + s[index+2:]
                index = max(0, index - 1)
            else:
                index += 1
        
        index = 0
        while index <= len(s) - 2:
            if s[index:index+2] == smaller_op:
                count += soa
                s = s[:index] + s[index+2:]
                index = max(0, index - 1)
            else:
                index += 1

        return count
            


if __name__ == '__main__':
    test_cases = ( ("cdbcbbaaabab", 4, 5, 19), ("aabbaaxybbaabb", 5, 4, 20))
    for case in test_cases:
        print('Input: ' + case[0] + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().maximumGain(case[0], case[1], case[2])) + '\n')