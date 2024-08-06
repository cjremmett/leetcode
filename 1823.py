class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]
        index = 0
        while len(friends) > 1:
            real_movement = (k % len(friends)) - 1
            index += real_movement
            index = index % len(friends)
            friends.pop(index)

        return friends[0]


if __name__ == '__main__':
    test_cases = ( (5, 2, 3), (6, 5, 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().findTheWinner(case[0], case[1])) + '\n')