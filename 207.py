from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjacency_list = {}
        for i in range(0, numCourses):
            self.adjacency_list[i] = []

        for course, prereq in prerequisites:
            self.adjacency_list[course].append(prereq)

        for course in self.adjacency_list:
            result = self.check_prereq_recursive(course, course)
            if result == False:
                return False
        
        return True

    
    def check_prereq_recursive(self, course, original):
        if course == original:
            return False

        for prereq in self.adjacency_list[course]:
            result = self.check_prereq_recursive(prereq, original)
            if result == False:
                return False

        
if __name__ == '__main__':
    test_cases = [(5, [[1,4],[2,4],[3,1],[3,2]], True), (2, [[1,0]], True), (2, [[1,0],[0,1]], False)]
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().canFinish(case[0], case[1])) + '\n')