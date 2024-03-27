from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        highest_amount = None
        current_amount = 0
        for num in nums:
            if current_amount + num >= num:
                current_amount += num
            else:
                current_amount = num

            if highest_amount == None:
                highest_amount = current_amount
            elif current_amount > highest_amount:
                highest_amount = current_amount

        return highest_amount

if __name__ == '__main__':
    test_cases = ( ([-2,1,-3,4,-1,2,1,-5,4], 6), ([5,4,-1,7,8], 23) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maxSubArray(case[0])) + '\n')