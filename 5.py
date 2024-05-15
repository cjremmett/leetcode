class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0]
        for i in range(0, len(s)):
            left = i
            right = i
            while True:
                if left - 1 >= 0 and right + 1 < len(s) and s[i-left] == s[i+right]:
                    left -= 1
                    right += 1
                elif right - left + 1 > len(max_palindrome):
                    max_palindrome = s[left:right+1]
                    break
                else:
                    break

        return max_palindrome
    
if __name__ == '__main__':
    test_cases = ( ("babad", ['bab', 'aba']), ("cbbd", ['bb']))
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + Solution().longestPalindrome(case[0]) + '\n')