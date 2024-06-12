from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)

        sentence = sentence.split(' ')
        for w in range(0, len(sentence)):
            for i in range(1, len(sentence[w])):
                if sentence[w][:i] in dictionary:
                    sentence[w] = sentence[w][:i]

        s = ' '
        return s.join(sentence)

if __name__ == '__main__':
    test_cases = ( (["cat","bat","rat"], "the cattle was rattled by the battery", "the cat was rat by the bat"), (["a","b","c"], "aadsfasf absbs bbab cadsfafs", "a a b c"))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + case[1] + '\nExpected output: ' + case[2] + '\nActual output: ' + Solution().replaceWords(case[0], case[1]) + '\n')