from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # priority_queue = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] >= priority_queue[0]:
        #         priority_queue.insert(0, nums[i])
        #     elif nums[i] <= priority_queue[-1]:
        #         priority_queue.append(nums[i])
        #     else:
        #         left = 0
        #         right = len(priority_queue) - 1
        #         while True:
        #             mid = left + ((right - left) // 2)
        #             if priority_queue[mid - 1] >= nums[i] and priority_queue[mid] <= nums[i]:
        #                 priority_queue.insert(mid, nums[i])
        #                 break
        #             elif priority_queue[mid] < nums[i]:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1

        # return priority_queue[k - 1]
        return (heapq.nlargest(k, nums))[-1]

if __name__ == '__main__':
    test_cases = ( ([3,2,1,5,6,4], 2, 5), ([3,2,3,1,2,4,5,5,6], 4, 4))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().findKthLargest(case[0], case[1])) + '\n')