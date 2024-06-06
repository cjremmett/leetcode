from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        group_array = []
        hand = sorted(hand)

        for num in hand:
            placed = False
            for group in group_array:
                if len(group) < groupSize and group[-1] == num - 1:
                    group.append(num)
                    placed = True
                    break
            
            if placed == False:
                group_array.append([num])

        if min(map(lambda x: len(x), group_array)) == groupSize:
            return True
        else:
            return False
    
if __name__ == '__main__':
    test_cases = ( ([1,2,3,6,2,3,4,7,8], 3, True), ([1,2,3,4,5], 4, False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().isNStraightHand(case[0], case[1])) + '\n')