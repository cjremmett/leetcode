from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for operation in logs:
            if operation == '../':
                depth = max(0, depth - 1)
            elif operation == './':
                pass
            else:
                depth += 1

        return depth


if __name__ == '__main__':
    test_cases = ( (["d1/","d2/","../","d21/","./"], 2), (["d1/","d2/","./","d3/","../","d31/"], 3), (["d1/","../","../","../"], 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minOperations(case[0])) + '\n')