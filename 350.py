from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = defaultdict(int)
        nums2_dict = defaultdict(int)

        for num in nums1:
            nums1_dict[num] += 1

        for num in nums2:
            nums2_dict[num] += 1

        ret_list = []
        for key in nums1_dict:
            for i in range(0, min(nums1_dict[key], nums2_dict[key])):
                ret_list.append(key)

        return ret_list


if __name__ == '__main__':
    test_cases = ( ([1,2,2,1], [2,2], [2,2]), ([4,9,5], [9,4,9,8,4], [4,9]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().intersect(case[0], case[1])) + '\n')