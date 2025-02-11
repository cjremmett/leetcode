class Solution:
    def clearDigits(self, s: str) -> str:
        nondigit_stack = []
        pointer = 0

        while pointer < len(s):
            o = ord(s[pointer])
            if o < 48 or o > 57:
                nondigit_stack.append(pointer)
                pointer += 1
            else:
                nd = nondigit_stack.pop()
                s = s[:nd] + s[nd + 1:pointer] + s[pointer + 1:]
                pointer -= 1

        return s


if __name__ == '__main__':
    test_cases = [ ["abc", "abc"], ["cb34", ""] ]
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + case[1] + '\nActual output: ' + Solution().clearDigits(case[0]) + '\n')

