class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}

        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        palindrome_len = 0
        used_one = False
        for key in counts:
            if counts[key] % 2 == 1:
                if used_one == False:
                    used_one = True
                    palindrome_len += counts[key]
                else:
                    palindrome_len += (counts[key] - 1)
            else:
                palindrome_len += counts[key]
        
        return palindrome_len

if __name__ == '__main__':
    test_cases = ( ("abccccdd", 7), ("a", 1))
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().longestPalindrome(case[0])) + '\n')