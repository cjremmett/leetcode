from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        group = []
        index = {}
        hand = sorted(hand)
        num_incomplete_groups = 0

        for num in hand:
            if num in index and len(index[num]) > 0:
                group_index = index[num][-1]
                group[group_index].append(num)
                if len(group[index[num][-1]]) < groupSize:
                    if num + 1 in index:
                        index[num+1].append(group_index)
                    else:
                        index[num+1] = [group_index]
                else:
                    num_incomplete_groups -= 1
                index[num].pop()
            else:
                group.append([num])
                num_incomplete_groups += 1
                if num + 1 in index:
                    index[num+1].append(len(group) - 1)
                else:
                    index[num+1] = [len(group) - 1]

        #if min(map(lambda x: len(x), group)) == groupSize:
        if num_incomplete_groups == 0:
            return True
        else:
            return False
    
if __name__ == '__main__':
    test_cases = ( ([1,2,3,6,2,3,4,7,8], 3, True), ([1,2,3,4,5], 4, False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().isNStraightHand(case[0], case[1])) + '\n')