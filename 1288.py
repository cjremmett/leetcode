from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -1 * x[1]))

        largest_end = intervals[0][1]
        current_start = intervals[0][0]
        count_removed = 0
        for interval in intervals[1:]:
            print(largest_end)
            print(current_start)
            print(f'{count_removed}\n')
            if interval[0] == current_start:
                count_removed += 1
                continue
            else:
                current_start = interval[0]
                if interval[1] <= largest_end:
                    count_removed += 1
                else:
                    largest_end = interval[1]

        return len(intervals) - count_removed
    

if __name__ == '__main__':
    test_cases = [([[1,4],[3,6],[2,8]], 2), ([[1,4],[2,3]], 1), ([[3,10],[4,10],[5,11]], 2)]
    for case in test_cases:
        print(f'Input: {case[0]}')
        print(f'Expected result: {case[1]}')
        print(f'Actual result: {Solution().removeCoveredIntervals(case[0])}')