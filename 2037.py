from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = 0
        seats.sort()
        students.sort()
        for i in range(0, len(seats)):
            count += abs(seats[i] - students[i])
        
        return count

if __name__ == '__main__':
    test_cases = ( ([3,1,5], [2,7,4], 4), ([4,1,5,9], [1,3,2,6], 7))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().minMovesToSeat(case[0], case[1])) + '\n')