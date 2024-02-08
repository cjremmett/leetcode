from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adjacency_list = {i:set() for i in range(0, numCourses)}
        
        for prereq in prerequisites:
            self.adjacency_list[prereq[1]].add(prereq[0])

        print(self.adjacency_list)

        return []
    

if __name__ == '__main__':
    test_cases = ( (2, [[1,0]], [0,1]), (4, [[1,0],[2,0],[3,1],[3,2]], [0,2,1,3]) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected Output: ' + str(case[2]) + '\nActual Output: ' + str(Solution().findOrder(case[0], case[1])) + '\n')