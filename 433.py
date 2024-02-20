from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        return 0


if __name__ == '__main__':
    test_cases = (["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1], ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2])
    for case in test_cases:
        print('Start gene: ' + case[0] + ' End gene: ' + case[1] + ' Bank: ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().minMutation(case[0], case[1], case[2])) + '\n')