from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [ [1], [1, 1] ]

        rows = [ [1], [1, 1] ]
        for i in range(3, numRows + 1):
            row = [1]
            for j in range(2, i):
                row.append(rows[i-2][j-2] + rows[i-2][j-1])
            row.append(1)
            rows.append(row)

        return rows

if __name__ == '__main__':
    test_cases = ( (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]), (1, [[1]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().generate(case[0])) + '\n')