class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        for start in nums:
            last = start
            count = 1
            for num in nums:
                if num == last + 1:
                    count += 1
                    last = num
            longest = max(count, longest)

        return longest