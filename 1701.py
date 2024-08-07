from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_times = []
        queued_wait_time = 0
        for i in range(0, len(customers)):
            if i != 0:
                queued_wait_time -= min(queued_wait_time, (customers[i][0] - customers[i-1][0]))
            queued_wait_time += customers[i][1]
            wait_times.append(queued_wait_time)
        
        sum_wait = sum(wait_times)
        return sum_wait / len(customers)


if __name__ == '__main__':
    test_cases = ([[1,2],[2,5],[4,3]], 5.0), ([[5,2],[5,4],[10,3],[20,1]], 3.25)
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().averageWaitingTime(case[0])) + '\n')