from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(positions) == 0:
            return []

        struct = self.get_sorted_robot_struct(positions, healths, directions)
        while(self.need_next_step(struct)):
            self.process_step(struct)

        struct.sort(key=lambda x:x[3])
        ret_list = [robot[1] for robot in struct]
        return ret_list

    
    def get_sorted_robot_struct(self, positions, healths, directions):
        struct = [[positions[i], healths[i], directions[i], i] for i in range(0, len(positions))]
        return sorted(struct, key=lambda x: x[0])


    def need_next_step(self, robot_struct):
        found_r = False
        for i in range(0, len(robot_struct)):
            cur_letter = robot_struct[i][2]
            if found_r == False and cur_letter == 'R':
                found_r = True
            elif found_r == True and cur_letter == 'L':
                return True
        return False

    
    def process_step(self, robot_struct):
        position = 0
        while position < len(robot_struct):
            if robot_struct[position][2] == 'L':
                robot_struct[position][0] -= 1
            if robot_struct[position][2] == 'R':
                robot_struct[position][0] += 1

            if robot_struct[position][2] == 'L' and position > 0:
                if robot_struct[position-1][0] == robot_struct[position][0]:
                    health = robot_struct[position][1] - robot_struct[position-1][1]
                    if health > 0:
                        robot_struct[position][1] -= 1
                        robot_struct.pop(position-1)
                        position += 1
                        continue
                    elif health < 0:
                        robot_struct[position-1][1] -= 1
                        robot_struct.pop(position)
                        continue
                    else:
                        robot_struct.pop(position)
                        robot_struct.pop(position-1)
                        continue
            elif robot_struct[position][2] == 'R' and position < len(robot_struct) - 1 and robot_struct[position+1][2] == 'L':
                if robot_struct[position+1][0] == robot_struct[position][0]:
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
                        robot_struct.pop(position)
                        robot_struct.pop(position+1)
                        continue
            else:
                position += 1


if __name__ == '__main__':
    test_cases = ( ([5,4,3,2,1], [2,17,9,15,10], "RRRRR", [2,17,9,15,10]), ([3,5,2,6], [10,10,15,12], "RLRL", [14]), ([1,2,5,6], [10,10,11,11], "RLRL", []))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + case[2] + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().survivedRobotsHealths(case[0], case[1], case[2])) + '\n')