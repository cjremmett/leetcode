from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = {}
        for i in range(0, len(arr1)):
            if arr1[i] in arr1_dict:
                arr1_dict[arr1[i]] += 1
            else:
                arr1_dict[arr1[i]] = 1

        arr1 = []
        for num in arr2:
            if num in arr1_dict:
                for i in range(0, arr1_dict[num]):
                    arr1.append(num)
                arr1_dict.pop(num)
            
        leftover_list = []
        for key in arr1_dict:
            for i in range(0, arr1_dict[key]):
                leftover_list.append(key)
            
        leftover_list.sort()

        return arr1 + leftover_list

if __name__ == '__main__':
    test_cases = ( ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6], [2,2,2,1,4,3,3,9,6,7,19]), ([28,6,22,8,44,17], [22,28,8,6], [22,28,8,6,17,44]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().relativeSortArray(case[0], case[1])) + '\n')