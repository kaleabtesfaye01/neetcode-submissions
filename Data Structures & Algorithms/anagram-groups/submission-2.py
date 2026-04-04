class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - create hashmap with sorted_str -> list of original strings structure
        - output all values as an array
        '''

        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())

        '''
        For n = len(strs), and k = max length of a string in strs
        TC: O(n * klogk)
        SC: O(n)
        '''