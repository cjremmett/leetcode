from typing import List
import heapq

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        unique_days = set()
        unique_days_ordered = []
        for day in bloomDay:
            if day not in unique_days:
                unique_days.add(day)
                heapq.heappush(unique_days_ordered, day)
        
        left = 0
        right = len(unique_days_ordered) - 1
        if not self.can_make_bouquets(bloomDay, m, k, unique_days_ordered[-1]):
            return -1
        while True:
            mid = (left + right) // 2
            if self.can_make_bouquets(bloomDay, m, k, unique_days_ordered[mid]):
                if (mid - 1 == -1 or not self.can_make_bouquets(bloomDay, m, k, mid - 1)):
                    return unique_days_ordered[mid]
                else:
                    right = mid - 1
            else:
                left = mid + 1

    
    def can_make_bouquets(self, bloomDay, m, k, target_day) -> bool:
        num_bouquets = 0
        count_bloomed = 0
        for day in bloomDay:
            if day <= target_day:
                count_bloomed += 1
                if count_bloomed == k:
                    num_bouquets += 1
                    if num_bouquets == m:
                        return True
                    count_bloomed = 0
            else:
                count_bloomed = 0
                
        return False

if __name__ == '__main__':
    test_cases = ( ([7,7,7,7,12,7,7], 2, 3, 12), ([1,10,10,3,2], 3, 1, 3), ([1,10,3,10,2], 3, 2, -1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().minDays(case[0], case[1], case[2])) + '\n')