from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        n1, n2 = len(nums1), len(nums2)
        visited = set()
        hp = []
        hp.append((nums1[0]+nums2[0],(0,0)))
        visited.add((0,0))
        count = 0
        while k and hp:
            val, (i,j) = heapq.heappop(hp)
            ans.append([nums1[i],nums2[j]])

            if i+1<n1 and (i+1,j) not in visited:
                heapq.heappush(hp, (nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))

            if j+1<n2 and (i, j+1) not in visited:
                heapq.heappush(hp,(nums1[i]+nums2[j+1], (i,j+1)))
                visited.add((i,j+1))

            k -= 1

        return ans
        
        # ans = []
        # left = 0
        # right = 0
        # ans.append([nums1[left], nums2[right]])
        # while len(ans) < k:
        #     if left + 1 < len(nums1):
        #         left_val = nums1[left + 1] + nums2[right]
        #     else:
        #         left_val = None

        #     if right + 1 < len(nums2):
        #         right_val = nums1[left] + nums2[right + 1]
        #     else:
        #         right_val = None

        #     if left_val == None:
        #         right += 1
        #         ans.append([nums1[left], nums2[right]])
        #     elif right_val == None:
        #         left += 1
        #         ans.append([nums1[left], nums2[right]])
        #     else:
        #         if left_val <= right_val:
        #             left += 1
        #             ans.append([nums1[left], nums2[right]])
        #         else:
        #             right += 1
        #             ans.append([nums1[left], nums2[right]])

        # return ans


    #     heap = []
    #     for i in range(0, len(nums1)):
    #         for j in range(0, len(nums2)):
    #             element = [nums1[i], nums2[j]]
    #             sum_element = nums1[i] + nums2[j]
    #             if len(heap) < k or sum_element < heap[0][0] + heap[0][1]:
    #                 self.binary_insert(heap, element)
    #                 if len(heap) > k:
    #                     heap.pop(0)

    #     return heap[::-1]


    # def binary_insert(self, array, element):
    #     left = 0
    #     right = len(array)
    #     if self.should_insert(array, element[0] + element[1], left) == 0:
    #         array.insert(0, element)
    #         return
    #     elif self.should_insert(array, element[0] + element[1], right) == 0:
    #         array.append(element)
    #         return
    #     while True:
    #         mid = left + ((right - left) // 2)
    #         result = self.should_insert(array, element[0] + element[1], mid)
    #         if result == 0:
    #             array.insert(mid, element)
    #             return
    #         elif result == -1:
    #             right = mid - 1
    #         else:
    #             left = mid + 1


    # def should_insert(self, array, element_sum, index):
    #     if index == 0 and (len(array) == 0 or element_sum >= array[0][0] + array[0][1]):
    #         return 0
    #     elif index == len(array) and element_sum <= array[-1][0] + array[-1][1]:
    #         return 0
    #     elif index == len(array) and element_sum > array[-1][0] + array[-1][1]:
    #         return -1
    #     elif element_sum >= array[index][0] + array[index][1]:
    #         return -1
    #     elif element_sum <= array[index][0] + array[index][1]:
    #         return 1
    #     else:
    #     #elif element_sum >= array[index][0] + array[index][1] and element_sum <= array[index - 1][0] + array[index - 1][1]:
    #         return 0

if __name__ == '__main__':
    test_cases = ( ([1,2,4,5,6], [3,5,7,9], 3, [[1,3],[2,3],[1,5]]), ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]), ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().kSmallestPairs(case[0], case[1], case[2])) + '\n')