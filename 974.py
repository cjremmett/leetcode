from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rems = {}
        sum = 0
        count_subs = 0

        for i in range(0, len(nums)):
            sum += nums[i]
            rem = abs(sum % k)
            if rem == 0:
                count_subs += 1

            if rem in rems:
                count_subs += len(rems[rem])
                rems[rem].append(i)
            else:
                rems[rem] = [i]
        
        return count_subs
    
if __name__ == '__main__':
    test_cases = ( ([4,5,0,-2,-3,1], 5, 7), ([5], 9 , 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().subarraysDivByK(case[0], case[1])) + '\n')