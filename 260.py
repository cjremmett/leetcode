from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen_set = set()
        result_set = set(nums)
        for num in nums:
            if num in seen_set:
                result_set.discard(num)
            else:
                seen_set.add(num)
                
        return list(result_set)
            

if __name__ == '__main__':
    test_cases = ( ([1,2,1,3,2,5], [3,5]), ([-1,0], [-1,0]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().singleNumber(case[0])) + '\n')