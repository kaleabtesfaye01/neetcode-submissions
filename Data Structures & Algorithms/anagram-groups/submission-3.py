class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - create hashmap with sorted_str -> list of original strings structure
        - output all values as an array
        '''

        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())

        '''
        For n = number of strings, and k = length of the longest string
        TC: O(n * klogk)
        SC: O(m * n)
        '''