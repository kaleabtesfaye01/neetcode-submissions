class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        n = len(nums)

        for i in range(n):
            start = nums[i]
            l = i+1
            r = n-1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum + start == 0:
                    triplets.add((start, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum + start > 0:
                    r -= 1
                else:
                    l += 1


        return [list(triplet) for triplet in triplets]