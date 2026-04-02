class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = defaultdict(int), defaultdict(int)

        for c in s:
            s_map[c] += 1
        
        for c in t:
            t_map[c] += 1
        
        return s_map == t_map