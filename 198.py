from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        s1 = nums[0] + nums[2]
        s2 = max(nums[0], nums[1])

        num_remaining = len(nums) - 3
        pointer = 2
        while True:
            if num_remaining >= 3:
                t1 = s1 + nums[pointer + 2]
                t2 = s1 + nums[pointer + 3]
                t3 = s2 + nums[pointer + 1] + nums[pointer + 3]
                t4 = max(s2 + nums[pointer + 1], s2 + nums[pointer + 2])
                if t1 >= t4:
                    temp1 = s1
                    temp1 += nums[pointer + 2]
                else:
                    temp1 = s2
                    temp1 += max(nums[pointer + 1], nums[pointer + 2])

                if t2 >= t3:
                    temp2 = s1
                    temp2 += nums[pointer + 3]
                else:
                    temp2 = s2
                    temp2 = temp2 + nums[pointer + 1] + nums[pointer + 3]

                s1, s2 = temp2, temp1
                num_remaining -= 3
                pointer += 3
            elif num_remaining == 2:
                return max(s1 + nums[pointer + 2], s2 + nums[pointer + 1], s2 + nums[pointer + 2])
            elif num_remaining == 1:
                return max(s1, s2 + nums[pointer + 1])
            else:
                return max(s1, s2)

if __name__ == '__main__':
    test_cases = ( ([8,4,8,5,9,6,5,4,4,10], 40), ([1,3,1,3,100], 103), ([2,7,9,3,1], 12), ([1,2,3,1], 4) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().rob(case[0])) + '\n')