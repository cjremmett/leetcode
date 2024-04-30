from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if i == 0 and j == 0:
                    heap.append([nums1[0], nums2[0]])
                    continue
                element = [nums1[i], nums2[j]]
                sum_element = nums1[i] + nums2[j]
                if sum_element < heap[0][0] + heap[0][1] or len(heap) < k:
                    self.binary_insert(heap, element)
                    if len(heap) > k:
                        heap.pop(0)

        return heap[::-1]


    def binary_insert(self, array, element):
        left = 0
        right = len(array)
        if self.should_insert(array, element[0] + element[1], left) == 0:
            array.insert(0, element)
            return
        elif self.should_insert(array, element[0] + element[1], right) == 0:
            array.append(element)
            return
        while True:
            mid = left + ((right - left) // 2)
            result = self.should_insert(array, element[0] + element[1], mid)
            if result == 0:
                array.insert(mid, element)
                return
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1


    def should_insert(self, array, element_sum, index):
        print(str(array) + ' ' + str(element_sum) + ' ' + str(index))
        if index == 0 and element_sum >= array[0][0] + array[0][1]:
            return 0
        elif index == len(array) and element_sum <= array[-1][0] + array[-1][1]:
            return 0
        elif index == len(array) and element_sum > array[-1][0] + array[-1][1]:
            return -1
        elif element_sum >= array[index][0] + array[index][1] and element_sum <= array[index - 1][0] + array[index - 1][1]:
            return 0
        elif element_sum >= array[index][0] + array[index][1]:
            return -1
        else:
            return 1

if __name__ == '__main__':
    test_cases = ( ([1,2,4,5,6], [3,5,7,9], 3, [[1,3],[2,3],[1,5]]), ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]), ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().kSmallestPairs(case[0], case[1], case[2])) + '\n')