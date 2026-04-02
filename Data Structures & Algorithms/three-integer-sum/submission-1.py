class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            start = nums[i]

            if start > 0:
                break

            if i > 0 and start == nums[i-1]:
                continue

            l,r = i+1, n-1

            while l < r:
                curr_sum = nums[l] + nums[r] + start
                if curr_sum == 0:
                    res.append([start, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
                    r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1


        return res