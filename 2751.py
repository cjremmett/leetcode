# Not solved

from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(positions) == 0:
            return []

        struct = self.get_sorted_robot_struct(positions, healths, directions)
        indices = self.get_rl_indices(struct)
        while(self.need_next_step(indices)):
            self.process_step(struct, indices)

        struct.sort(key=lambda x:x[3])
        ret_list = [robot[1] for robot in struct]
        return ret_list


    def get_rl_indices(self, robot_struct):
        left_indices = {}
        right_indices = {}
        for i in range(0, len(robot_struct)):
            left_indices[robot_struct[i][0]] = robot_struct[i][2]
        
        return (left_indices, right_indices)

    
    def get_sorted_robot_struct(self, positions, healths, directions):
        struct = [[positions[i], healths[i], directions[i], i] for i in range(0, len(positions))]
        return sorted(struct, key=lambda x: x[0])


    def need_next_step(self, indices):
        if len(indices[0]) == 0 or len(indices[1]) == 0 or indices[1][0] > indices[0][-1]:
            return False
        else:
            return True

    
    def process_step(self, robot_struct, indices):
        position = 0
        while position < len(robot_struct):
            if robot_struct[position][2] == 'L':
                robot_struct[position][0] -= 1
            if robot_struct[position][2] == 'R':
                robot_struct[position][0] += 1

            if robot_struct[position][2] == 'L' and position > 0 and robot_struct[position-1][0] == robot_struct[position][0]:
                health = robot_struct[position][1] - robot_struct[position-1][1]
                if health > 0:
                    robot_struct[position][1] -= 1
                    robot_struct.pop(position-1)
                    continue
                elif health < 0:
                    robot_struct[position-1][1] -= 1
                    robot_struct.pop(position)
                    continue
                else:
                    robot_struct.pop(position)
                    robot_struct.pop(position-1)
                    position -= 1
                    continue
            elif robot_struct[position][2] == 'R' and position < len(robot_struct) - 1 and robot_struct[position+1][2] == 'L' and robot_struct[position+1][0] == robot_struct[position][0]:
                health = robot_struct[position][1] - robot_struct[position+1][1]
                if health > 0:
                    robot_struct[position][1] -= 1
                    robot_struct.pop(position+1)
                    position += 1
                    continue
                elif health < 0:
                    robot_struct[position+1][1] -= 1
                    robot_struct.pop(position)
                    continue
                else:
                    robot_struct.pop(position+1)
                    robot_struct.pop(position)
                    continue
            else:
                position += 1


if __name__ == '__main__':
    test_cases = ( ([43,37,25,29,9,20,24,22], [40,1,44,28,47,7,15,45], "RLLRRRLL", [40,27,44]), ([4,48,23,42], [16,25,26,16], "LLLR", [16,24,26]), ([5,46,12], [3,27,43], "RLL", [27,42]), ([1,2,5,6], [10,10,11,11], "RLRL", []), ([5,4,3,2,1], [2,17,9,15,10], "RRRRR", [2,17,9,15,10]), ([3,5,2,6], [10,10,15,12], "RLRL", [14]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + case[2] + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().survivedRobotsHealths(case[0], case[1], case[2])) + '\n')