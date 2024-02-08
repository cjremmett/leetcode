from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(list)
        self.results = []

        for i in range(0, len(equations)):
            self.graph[equations[i][0]].append((equations[i][1], values[i]))
            self.graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        for query in queries:
            if query[0] not in self.graph or query[1] not in self.graph:
                self.results.append(-1.0)
            elif query[0] == query[1]:
                self.results.append(1.0)
            else:
                self.results.append(self.process_query(query[0], query[1], 1, set()))

        return self.results
    
    def process_query(self, start, end, count, already_seen):
        if start in already_seen:
            return -1.0
        else:
            already_seen.add(start)

        if start == end:
            return count
        else:
            for edge in self.graph[start]:
                result = self.process_query(edge[0], end, count * edge[1], already_seen.copy())
                if result != -1.0:
                    return result
                
        return -1.0


if __name__ == '__main__':
    test_cases = (([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]), ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + ' ' + str(case[2]) + '\nExpected Output: ' + str(case[3]) + '\nActual Output: ' + str(Solution().calcEquation(case[0], case[1], case[2])) + '\n')