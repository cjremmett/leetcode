from typing import List
import heapq

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        unique_days = set(bloomDay)
        unique_days_ordered = list(unique_days)
        unique_days_ordered.sort()
        
        left = 0
        right = len(unique_days_ordered) - 1
        if not self.can_make_bouquets(bloomDay, m, k, unique_days_ordered[-1]):
            return -1
        while True:
            mid = (left + right) // 2
            if self.can_make_bouquets(bloomDay, m, k, unique_days_ordered[mid]):
                if (mid - 1 == -1 or not self.can_make_bouquets(bloomDay, m, k, unique_days_ordered[mid] - 1)):
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
    test_cases = ( ([3542,4862,3568,3602,2074,2056,1330,923,2362,4948,1403,1208,5554,2591,2567,4857,266,4274,4995,863,4167,3389,2515,2778,955,5152,4232,4154,2041,5169,574,4786,3096,252,2501,1397,1910,2722,3116,2707,2837,409,488,2048,2546,4196,580,4434,2361,5190,4842,4914,487,3047,1676,3716,737,5378,244,3565,7,3672,4115,3985,123,4708,1701,5649,3961,1138,1254,3692,366,4342,4225,1240,2286,986,4111,1247,2992,5391,4497,1472,241,4530,4416,1842,1590,4607,588,3379,1895,5364,4133,418,1387,5113,3352,4965,4909,2216,1295,4531,4171,3224,5407,1654,3142,4662,444,1538,1431,844,2759,2735,3760,2605,1546,3630,4066,1870,410,3858,480,2389,1905,3553,638,1606,1786,1804,3355,2898,1126,108,908,4194,4782,2619,272,20,5102,4344,3158,1867,2484,1462,4269,1382,2215,3233,3425,3435,401,4660,5201,317,5149,1249,2070,5309,846,2839,1738,3207,1155,4055,702,3625,3561,4486,5652,2224,185,3269,2144,1757,3861,302,3431,5481,2042,2979,3915,3935,1976,1347,1360,3445,1733,3334,1252,5310,1557,4471,4836,993,2441,3554,2204,2884,3645,279,1346,2783,3013,1531,1066,4635,5630,4235,2655,4981,1781,353,3809,382,370,2352,2815,935,634,4329,5396,5420,3199,2868,1583,839,468,5320,5572,4319,4026,1632,3930,682,5059,2066,1078,1225,801,3306,278,52,4287,1857,1214,668,3770,1445,4143,5332,1037,277,4646,1118,4473,5238,3528,2294,246,514,2395,4101,2244,731,2975,973], 11, 11, 4948), ([1,10,2,9,3,8,4,7,5,6], 4, 2, 9), ([7,7,7,7,12,7,7], 2, 3, 12), ([1,10,10,3,2], 3, 1, 3), ([1,10,3,10,2], 3, 2, -1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().minDays(case[0], case[1], case[2])) + '\n')