from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_ops = 0
        nums.sort(key = lambda x: x * -1)
        while nums[-1] < k:
            x = nums.pop()
            y = nums.pop()
            insert = min(x, y) * 2 + max(x, y)

            lp = 0
            rp = len(nums) - 1
            while true:
                mid = (lp + rp) // 2
                if mid == 0 and insert >= nums[mid]:
                    nums.insert(0, insert)
                elif mid == len(nums) - 1 and insert <= nums[-1]:
                    nums.append(insert)


if __name__ == '__main__':
    test_cases = [ [[2,11,10,1,3], 10, 2], [[1,1,2,4,9], 20, 4]]
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minOperations(case[0], case[1])) + '\n')
