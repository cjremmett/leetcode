from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_min_mag = (position[-1] - 1) // (m - 1)
        left = 1
        right = max_min_mag
        if not self.can_meet_min(position, m, left):
            return -1
        else:
            while True:
                mid = (left + right) // 2
                mid_passed = self.can_meet_min(position, m, mid)
                mid_plus_one_passed = self.can_meet_min(position, m, mid + 1)
                if mid_passed and not mid_plus_one_passed:
                    return mid
                elif not mid_passed:
                    right = mid - 1
                else:
                    left = mid + 1
                

    
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
    test_cases = ( ([269826447,974181916,225871443,189215924,664652743,592895362,754562271,335067223,996014894,510353008,48640772,228945137], 3, 0), ([1,2,3,4,7], 3, 3), ([5,4,3,2,1,1000000000], 2, 999999999))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().maxDistance(case[0], case[1])) + '\n')