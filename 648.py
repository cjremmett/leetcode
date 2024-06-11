from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictset = set(dictionary)

if __name__ == '__main__':
    test_cases = ( (["cat","bat","rat"], "the cattle was rattled by the battery", "the cat was rat by the bat"), (["a","b","c"], "aadsfasf absbs bbab cadsfafs", "a a b c"))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + case[1] + '\nExpected output: ' + case[2] + '\nActual output: ' + Solution().replaceWords(case[0], case[1]) + '\n')