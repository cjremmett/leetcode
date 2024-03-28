from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        looped_already = False
        start_index = None
        i = 0
        current_sum = None
        best_sum = None
        while True:
            if i == len(nums):
                if looped_already == True:
                    break
                else:
                    looped_already = True
                i = 0
                continue

            if start_index != None and i == start_index:
                break

            if current_sum == None or nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                start_index = i
            else:
                current_sum += nums[i]
            
            if best_sum == None or best_sum < current_sum:
                best_sum = current_sum

            i += 1

        return best_sum


if __name__ == '__main__':
    test_cases = ( ([5,-3,5], 10), ([1,-2,3,-2], 3), ([-3,-2,-3], -2))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maxSubarraySumCircular(case[0])) + '\n')