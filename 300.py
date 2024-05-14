from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        segments = []
        for num in nums:
            old_segments = segments.copy()
            segments.append([1, num])
            for segment in old_segments:
                if num > segment[1]:
                    segments.append(segment.copy())
                    segment[0] += 1
                    segment[1] = num
    
        return max(map(lambda x: x[0], segments))


if __name__ == '__main__':
    test_cases = ( ([0,1,0,3,2,3], 4), ([10,9,2,5,3,7,101,18], 4), ([7,7,7,7,7,7,7], 1) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().lengthOfLIS(case[0])) + '\n')