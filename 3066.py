from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_ops = 0
        nums.sort(key = lambda x: x * -1)
        while nums[-1] < k:
            num_ops += 1
            print(str(nums))
            x = nums.pop()
            y = nums.pop()
            insert = min(x, y) * 2 + max(x, y)

            lp = 0
            rp = len(nums) - 1
            while True:
                if len(nums) == 0:
                    nums.append(insert)
                    return num_ops
                mid = (lp + rp) // 2
                #print("left: " + str(lp) + ' right: ' + str(rp) + ' Mid: ' + str(mid) + ' Nums: ' + str(nums) + ' Insert: ' + str(insert))
                if(num_ops > 5):
                    return 0
                if mid == 0:
                    if insert >= nums[mid]:
                        nums.insert(0, insert)
                    else:
                        lp += 1
                else:
                    if insert > nums[mid - 1]:
                        rp = mid - 1
                    elif insert < nums[mid]:
                        lp = mid + 1
                    else:
                        nums.insert(mid, insert)
                        break

        return num_ops




if __name__ == '__main__':
    test_cases = [ [[2,11,10,1,3], 10, 2], [[1,1,2,4,9], 20, 4]]
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().minOperations(case[0], case[1])) + '\n')
