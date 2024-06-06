class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer = 0
        num_found = 0
        for i in range(0, len(t)):
            while s[pointer] != t[i]:
                pointer += 1
                if pointer >= len(s):
                    return len(t) - num_found
            
            num_found += 1
            pointer += 1
            if num_found == len(t):
                return 0
            if pointer >= len(s):
                return len(t) - num_found

if __name__ == '__main__':
    test_cases = ( ("lxvqffcj", "vjtgatotj", 7), ("zbc", "abc", 3), ("coaching", "coding", 4), ("abcde", "a", 0), ("z", "abcde", 5))
    for case in test_cases:
        print('Input: ' + case[0] + ' ' + case[1] + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().appendCharacters(case[0], case[1])) + '\n')