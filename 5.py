class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0]
        for i in range(0, len(s)):
            left = i
            right = i
            while True:
                if left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                elif right - left + 1 > len(max_palindrome):
                    max_palindrome = s[left:right+1]
                    break
                else:
                    break

        for i in range(1, len(s)):
            left = i - 1
            right = i
            while True:
                if left - 1 >= 0 and right + 1 < len(s) and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                elif right - left + 1 > len(max_palindrome) and s[left:right+1] == s[left:right+1][::-1]:
                    max_palindrome = s[left:right+1]
                    break
                else:
                    break

        return max_palindrome
    
if __name__ == '__main__':
    test_cases = ( ("cbbd", ['bb']), ("babad", ['bab', 'aba']))
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + Solution().longestPalindrome(case[0]) + '\n')