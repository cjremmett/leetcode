from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.largest_list = [None for i in range(0, k)]

        for i in range(0, len(nums)):
            self.insert_into_largest_list(nums[i], k)

        return self.largest_list[k - 1]
        
    def insert_into_largest_list(self, num, k):
        for i in range(0, len(self.largest_list)):
            if self.largest_list[i] == None or num >= self.largest_list[i]:
                self.largest_list.insert(i, num)
                break
        
        if len(self.largest_list) > k:
            self.largest_list.pop()


    

if __name__ == '__main__':
    test_cases = ( ([3,2,1,5,6,4], 2, 5), ([3,2,3,1,2,4,5,5,6], 4, 4))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().findKthLargest(case[0], case[1])) + '\n')