from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 0
        b = 0
        current_mod = 10
        while n > 0:
            insert = n % current_mod
            current_mod *= 10
            n = n - insert

            if insert == 0:
                continue
            elif insert == 1:
                a += 1
            else:
                for i in range(1, insert):
                    a_insert = i
                    b_insert = insert - a_insert

                    a_post_insertion = a + a_insert
                    b_post_insertion = b + b_insert

                    if('0' not in str(a_post_insertion) and '0' not in str(b_post_insertion)):
                        a = a_post_insertion
                        b = b_post_insertion
                        break

        return [a, b]
    

if __name__ == '__main__':
    test_cases = ( (2, [1, 1]), (11, [9, 2]))
    for case in test_cases:
        print(f'Input: {case[0]}\nPossible output: {case[1]}\nActual output: {Solution().getNoZeroIntegers(case[0])}\n')