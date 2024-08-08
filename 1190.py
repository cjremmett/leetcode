class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                start = stack.pop()
                end = i
                s = s[:start] + s[start:end+1][::-1] + s[end+1:]

        s = s.replace('(', '')
        s = s.replace(')', '')
        return s 

if __name__ == '__main__':
    test_cases = ( ("(abcd)", "dcba"), ("(u(love)i)", "iloveu"), ("(ed(et(oc))el)", "leetcode"))
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + case[1] + '\nActual output: ' + Solution().reverseParentheses(case[0]) + '\n')