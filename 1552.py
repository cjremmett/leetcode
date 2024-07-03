from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_min_mag = (position[-1] - 1) // (m - 1)
        for i in reversed(range(1, max_min_mag + 1)):
            if self.can_meet_min(position, m, i):
                return i

        return -1

    
    def can_meet_min(self, position, m, maxmin) -> bool:
        prev_ball_pos = position[0]
        pointer = 1
        num_balls_placed = 1
        while True:
            if num_balls_placed == m:
                return True

            if pointer >= len(position):
                return False

            if position[pointer] - prev_ball_pos >= maxmin:
                prev_ball_pos = position[pointer]
                pointer += 1
                num_balls_placed += 1
            else:
                pointer += 1

if __name__ == '__main__':
    test_cases = ( ([1,2,3,4,7], 3, 3), ([5,4,3,2,1,1000000000], 2, 999999999))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().maxDistance(case[0], case[1])) + '\n')