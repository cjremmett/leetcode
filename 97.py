class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) == 0:
            return True
        if len(s1) + len(s2) != len(s3):
            return False

        possible_solutions = set()
        possible_solutions = [('', 0, 0)]
        possible_solutions_temp = set()

        for i in range(0, len(s3)):
            if len(possible_solutions) == 0:
                return False

            for possible_solution in possible_solutions:
                if possible_solution[1] < len(s1) and s3[i] == s1[possible_solution[1]]:
                    if possible_solution[0] + s3[i] == s3:
                        return True
                    possible_solutions_temp.add((possible_solution[0] + s3[i], possible_solution[1] + 1, possible_solution[2]))
                
                if possible_solution[2] < len(s2) and s3[i] == s2[possible_solution[2]]:
                    if possible_solution[0] + s3[i] == s3:
                        return True
                    possible_solutions_temp.add((possible_solution[0] + s3[i], possible_solution[1], possible_solution[2] + 1))

            possible_solutions = possible_solutions_temp
            possible_solutions_temp = set()
            print(len(possible_solutions))

        return False

if __name__ == '__main__':
    test_cases = ( ("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc", True), ("aabcc", "dbbca", "aadbbcbcac", True), ("aabcc", "dbbca", "aadbbbaccc", False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().isInterleave(case[0], case[1], case[2])) + '\n')