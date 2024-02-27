from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.combinations = set()
        self.next_iteration('', digits, 0)
        #return sorted(list(self.combinations))
        self.combinations.discard('')
        return self.combinations

    def next_iteration(self, progress_so_far, digits, next_index_in_digits):
        if next_index_in_digits >= len(digits):
            self.combinations.add(progress_so_far)
            return
        else:
            digit = digits[next_index_in_digits]
            match(digit):
                case('2'):
                    self.next_iteration(progress_so_far + 'a', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'b', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'c', digits, next_index_in_digits + 1)
                case('3'):
                    self.next_iteration(progress_so_far + 'd', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'e', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'f', digits, next_index_in_digits + 1)
                case('4'):
                    self.next_iteration(progress_so_far + 'g', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'h', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'i', digits, next_index_in_digits + 1)
                case('5'):
                    self.next_iteration(progress_so_far + 'j', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'k', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'l', digits, next_index_in_digits + 1)
                case('6'):
                    self.next_iteration(progress_so_far + 'm', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'n', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'o', digits, next_index_in_digits + 1)
                case('7'):
                    self.next_iteration(progress_so_far + 'p', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'q', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'r', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 's', digits, next_index_in_digits + 1)
                case('8'):
                    self.next_iteration(progress_so_far + 't', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'u', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'v', digits, next_index_in_digits + 1)
                case('9'):
                    self.next_iteration(progress_so_far + 'w', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'x', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'y', digits, next_index_in_digits + 1)
                    self.next_iteration(progress_so_far + 'z', digits, next_index_in_digits + 1)

if __name__ == '__main__':
    test_cases = (['7', [["p","q","r","s"]]], ['23', ["ad","ae","af","bd","be","bf","cd","ce","cf"]], ['', []], ['2', ["a","b","c"]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().letterCombinations(case[0])))