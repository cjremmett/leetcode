from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = []
        # for n in nums:
        #     ind = bisect.bisect_left(dp, n)
        #     if ind == len(dp):
        #         dp.append(n)
        #     else:
        #         dp[ind] = n
        # return len(dp)
        dp = [1 for x in nums]
        for i in range(0, len(nums)):
            segmax = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    segmax = max(segmax, dp[j] + 1)
            
            dp[i] = segmax

        return max(dp)



if __name__ == '__main__':
    test_cases = ( ([0,1,0,3,2,3], 4), ([10,9,2,5,3,7,101,18], 4), ([7,7,7,7,7,7,7], 1) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().lengthOfLIS(case[0])) + '\n')