from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        num_moves_left = 0
        num_moves_right = 0
        num_balls_left = 0
        num_balls_right = 0
        pointer = 0
        
        results = []

        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                num_moves_right += i
                num_balls_right += 1
        
        while pointer < len(boxes):
            results.append(num_moves_left + num_moves_right)

            if boxes[pointer] == '1':
                num_balls_left += 1
            
            num_moves_left += num_balls_left

            pointer += 1
            if pointer == len(boxes):
                return results

            num_moves_right -= num_balls_right
            if boxes[pointer] == '1':
                num_balls_right -= 1

            

if __name__ == '__main__':
    test_cases = [ ["110", [1,1,3]], ["001011", [11,8,5,4,3,4]]]
    for case in test_cases:
        print('Input: ' + case[0] + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minOperations(case[0])) + '\n')