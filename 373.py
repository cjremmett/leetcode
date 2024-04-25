from typing import List
import heapq

# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         heap = []
#         for i in range(0, len(nums1)):
#             for j in range(0, len(nums2)):
#                 sum = nums1[i] + nums2[j]
#                 if len(heap) < k:


#     def binary_insert(self, array, element):
#         left = 0
#         right = len(array)
#         while True:
            

#     def should_insert(self, array, element_sum, index):
#         if index == 0 and element_sum >= array[0][0] + array[0][1]:
#             return 0
#         elif index = len(array) and element_sum <= array[-1][0] + array[-1][1]:
#             return 0
#         elif element_sum >= array[index][0] + array[index][1] and element_sum <= array[index - 1][0] + array[index - 1][1]:
#             return 0
#         elif element_sum >= array[index][0] + array[index][1]:
#             return -1
#         else:
#             return 1

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        left = 0
        right = 0
        array = []
        while len(array) < k:
            array.append([nums1[left], nums2[right]])
            if left == len(nums1) - 1:
                right += 1
            elif right == len(nums2) -1:
                left += 1
            elif nums1[left + 1] > nums2[right + 1]:
                right += 1
            else:
                left += 1

        return array

if __name__ == '__main__':
    test_cases = ( ([1,2,4,5,6], [3,5,7,9], 3, [[1,3],[2,3],[1,5]]), ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]), ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().kSmallestPairs(case[0], case[1], case[2])) + '\n')