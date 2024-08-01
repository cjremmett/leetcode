class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        still_playing = set()
        for i in range(0, n):
            still_playing.add(i)

        friends = {i:True for i in range(1, n + 1)}
        cur_friend = 1
        while len(still_playing) > 1:
            real_movement = k % len(still_playing)
            for i in range(0, real_movement):
                while friends[cur_friend] == False:
                    cur_friend += 1
            friends[cur_friend] = False
            still_playing.discard(cur_friend)

        return list(still_playing[0])


if __name__ == '__main__':
    test_cases = ( (5, 2, 3), (6, 5, 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().findTheWinner(case[0], case[1])) + '\n')