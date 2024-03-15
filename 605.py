from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n < 1:
            return True
        
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
        count_zeros = 0
        count_flowers = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                count_zeros = 0
            elif flowerbed[i] == 0:
                count_zeros += 1
                if count_zeros == 3:
                    count_flowers += 1
                    count_zeros = 1
                    if count_flowers >= n:
                        return True
                    
        return False
    

if __name__ == '__main__':
    test_cases = ( ([0,0,1,0,1], 1, True), ([1,0,0,0,1], 1, True), ([1,0,0,0,1], 2, False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().canPlaceFlowers(case[0], case[1])) + '\n')