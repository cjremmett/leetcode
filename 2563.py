from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) < 2:
            return 0
        
        num_fair_pairs = 0
        list_seen = []
        for num in nums:
            lower_bound_fair = lower - num
            upper_bound_fair = upper - num
            lbfi = bisect.bisect_left(list_seen, lower_bound_fair)
            ubfi = bisect.bisect_right(list_seen, upper_bound_fair)
            num_fair_pairs += ubfi - lbfi
            list_seen.insert(bisect.bisect_left(list_seen, num), num)
        
        return num_fair_pairs
    

if __name__ == '__main__':
    test_cases = ( ([0,1,7,4,4,5], 3, 6, 6), ([1,7,9,2,5], 11, 11, 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().countFairPairs(case[0], case[1], case[2])) + '\n')