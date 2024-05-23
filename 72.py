import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        dp_temp = []
        positions = defaultdict(list)
        for i in range(0, len(word2)):
            positions[word2[i]].append(i)
        
        for i in range(0, len(word1)):
            for index in positions[word1[i]]:
                dp.append([word1[i], index])

            for combo in dp:
                for index in positions[word1[i]]:
                    if index > combo[1]:
                        dp_temp.append([combo[0] + word1[i], index])

            dp.append(dp_temp)
            dp_temp = []

        return max(map(lambda x: x[1], dp)) + abs(len(word1) - len(word2))

if __name__ == '__main__':
    test_cases = ( ("horse", "ros", 3), ("intention", "execution", 5))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().minDistance(case[0], case[1])) + '\n')