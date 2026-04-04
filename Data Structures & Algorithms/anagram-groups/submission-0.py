class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - create hashmap with sorted_str -> list of original strings structure
        - output all values as an array
        '''

        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            anagram_map[''.join(sorted_s)].append(s)

        return [anagram_group for anagram_group in anagram_map.values()]