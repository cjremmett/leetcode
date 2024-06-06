from typing import List
from collections import defaultdict

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_dicts = []

        for word in words:
            counts = defaultdict(int)
            for char in word:
                counts[char] += 1
            word_dicts.append(counts)

        results = []
        for i in range(65, 123):
            char = chr(i)
            val = min(map(lambda x: x[char], word_dicts))
            for i in range(0, val):
                results.append(char)

        return results


if __name__ == '__main__':
    test_cases = ( (["bella","label","roller"], ["e","l","l"]), (["cool","lock","cook"], ["c","o"]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().commonChars(case[0])) + '\n')