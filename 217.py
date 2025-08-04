from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in range(0, len(nums)):
            if nums[i] in num_set:
                return True
            else:
                num_set.add(nums[i])
        
        return False


if __name__ == '__main__':
    test_cases = ( ([1,2,3,1], True), ([1,2,3,4], False), ([1,1,1,3,3,4,3,2,4,2], True))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected Output: {case[1]}\nActual output: {Solution().containsDuplicate(case[0])}\n')