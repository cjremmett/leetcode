from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rems = {}
        sum = 0

        for i in range(0, len(nums)):
            sum += nums[i]
            rem = sum % k
            if (rem == 0 and i > 0) or (rem in rems and i >= rems[rem] + 2):
                return True
            else:
                if rem not in rems:
                    rems[rem] = i
        
        return False
    
    def brute_force(self, nums, k):
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i != j and sum(nums[i:j]) % k == 0:
                    return i, j


if __name__ == '__main__':
    test_cases = ( ([422,224,184,178,189,290,196,236,281,464,351,193,49,76,0,298,193,176,158,514,312,143,475,322,206,67,524,424,76,99,473,256,364,292,141,186,190,69,433,205,93,72,476,393,512,468,160,201,226,394,47,140,389,51,142,135,349,244,16,356,440,188,16,133,58,394,7,517,56,480,400,146,169,439,102,374,370,242,4,264,120,218,196,173,215,411,501,321,319,147,369,458,319,174,379,46,129,353,330,101], 479, True), ([23,2,4,6,7], 6, True), ([23,2,6,4,7], 6, True), ([23,2,6,4,7], 13, False))
    for case in test_cases:
        #print(str(Solution().brute_force(case[0], case[1])))
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().checkSubarraySum(case[0], case[1])) + '\n')