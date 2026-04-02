class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq_map[num] += 1
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
