from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        bitwise_dict = {}
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if j >= i:
                    if j == i:
                        bitwise_dict[(i, j)] = arr[i]
                    else:
                        nums = arr[i:j+1]
                        start = nums[0]
                        for k in range(1, len(nums)):
                            start ^= nums[k]
                        bitwise_dict[(i, j)] = start
        
        results = 0
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                for k in range(0, len(arr)):
                    if i < j and j <= k:
                        if bitwise_dict[(i, j-1)] == bitwise_dict[(j, k)]:
                            results += 1

        return results

if __name__ == '__main__':
    test_cases = ( ([2,3,1,6,7], 4), ([1,1,1,1,1], 10))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().countTriplets(case[0])) + '\n')