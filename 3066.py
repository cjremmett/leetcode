from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_ops = 0
        nums.sort(key = lambda x: x * -1)
        while nums[-1] < k:
            num_ops += 1
            #print(str(nums))
            x = nums.pop()
            y = nums.pop()
            insert = min(x, y) * 2 + max(x, y)

            lp = 0
            rp = len(nums) - 1
            while True:
                if len(nums) == 0:
                    nums.append(insert)
                    return num_ops
                elif len(nums) == 1:
                    if nums[0] > insert:
                        nums.append(insert)
                        break
                    else:
                        nums.insert(0, insert)
                        break
                mid = (lp + rp) // 2
                #print(str(mid) + ' ' + str(lp) + ' ' + str(rp))
                if mid == 0:
                    if insert >= nums[mid]:
                        nums.insert(0, insert)
                        break
                    else:
                        lp += 1
                else:
                    if insert > nums[mid - 1]:
                        rp = mid - 1
                    elif insert < nums[mid]:
                        if mid == len(nums) - 1:
                            nums.append(insert)
                            break
                        else:
                            lp = mid + 1
                    else:
                        nums.insert(mid, insert)
                        break

        return num_ops




if __name__ == '__main__':
    test_cases = [ [[2,11,10,1,3], 10, 2], [[1,1,2,4,9], 20, 4], [[1000000000,999999999,1000000000,999999999,1000000000,999999999], 1000000000, 2], [[85,93,100,90,40,7,62,90,68,88], 88, 3]]
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().minOperations(case[0], case[1])) + '\n')
