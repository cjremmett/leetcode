import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        best_combinations = []
        chars = defaultdict(list)
        for i in range(0, len(word1)):
            chars[word1[i]].append(i)

        for i in range(0, len(word2)):
            for index in chars[word2[i]]:
                best_combinations.append([])

if __name__ == '__main__':
    test_cases = ( ("horse", "ros", 3), ("intention", "execution", 5))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().minDistance(case[0], case[1])) + '\n')