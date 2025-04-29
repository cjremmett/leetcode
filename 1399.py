from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for i in range(1, n+1):
            s = str(i)
            num_sum = 0
            for j in range(0, len(s)):
                num_sum += int(s[j])
            groups[num_sum] += 1

        counts = defaultdict(int)
        for count in groups.values():
            counts[count] += 1

        return counts[max(list(counts.keys()))]
    

if __name__ == '__main__':
    test_cases = ( (13, 4), (2, 2))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().countLargestGroup(case[0])) + '\n')