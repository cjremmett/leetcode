from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adjacency_list = {i:set() for i in range(0, numCourses)}
        
        for prereq in prerequisites:
            self.adjacency_list[prereq[0]].add(prereq[1])

        self.course_order = []
        self.visited = set()
        self.circular = False

        for course in self.adjacency_list:
            self.topological_traverse(course, set())
         
        if self.circular == True:
            return []
        else:
            return self.course_order
    
    def topological_traverse(self, course, already_seen):
        if course in already_seen:
            self.circular = True
            return
        elif course in self.visited or self.circular == True:
            return
        else:
            already_seen.add(course)
            self.visited.add(course)
            for prereq in self.adjacency_list[course]:
                self.topological_traverse(prereq, already_seen.copy())
            self.course_order.append(course)

if __name__ == '__main__':
    test_cases = ( (3, [[0,2],[1,2],[2,0]], []), (2, [[1,0],[0,1]], []), (3, [[0,1],[0,2],[1,2]], [2,1,0]), (2, [[1,0]], [0,1]), (4, [[1,0],[2,0],[3,1],[3,2]], [0,2,1,3]) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected Output: ' + str(case[2]) + '\nActual Output: ' + str(Solution().findOrder(case[0], case[1])) + '\n')