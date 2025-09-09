from collections import defaultdict
from typing import List

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        num_aware_of_secret = 1
        num_sharing_secret = 0
        days = defaultdict(List[int, int])
        for i in range(1, n + 1):
            num_sharing_secret += days[i][0]
            days[i + delay][0] += num_sharing_secret
            days[i + forget][1] += 
    

if __name__ == '__main__':
    test_cases = ( (6, 2, 4, 5), (4, 1, 3, 6))
    for case in test_cases:
        print(f'Input: {case[0]}, {case[1]}, {case[2]}\nExpected output: {case[3]}\nActual output: {Solution().peopleAwareOfSecret(case[0], case[1], case[2])}\n')