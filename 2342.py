from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_dict = {}
        highest = -1
        for num in nums:
            sum = 0
            for digit in str(num):
                sum += int(digit)

            if sum in sum_dict:
                if len(sum_dict[sum]) == 1:
                    if num > sum_dict[sum][0]:
                        sum_dict[sum].insert(0, num)
                    else:
                        sum_dict[sum].append(num)
                else:
                    if num > sum_dict[sum][0]:
                        sum_dict[sum][1] = sum_dict[sum][0]
                        sum_dict[sum][0] = num
                    elif num > sum_dict[sum][1]:
                        sum_dict[sum][1] = num

                if sum_dict[sum][0] + sum_dict[sum][1] > highest:
                    highest = sum_dict[sum][0] + sum_dict[sum][1]
            else:
                sum_dict[sum] = [num]

        return highest

if __name__ == '__main__':
    test_cases = [ [[18,43,36,13,7], 54 ], [[10,12,19,14], -1] ]
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maximumSum(case[0])) + '\n')
