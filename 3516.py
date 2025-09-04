class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance_one = abs(z - x)
        distance_two = abs(z - y)
        if distance_one < distance_two:
            return 1
        elif distance_two < distance_one:
            return 2
        else:
            return 0
    

if __name__ == '__main__':
    test_cases = ( ((2, 7, 4), 1), ((2, 5, 6), 2), ((1, 5, 3), 0))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected output: {case[1]}\nActual output: {Solution().findClosest(case[0][0], case[0][1], case[0][2])}\n')