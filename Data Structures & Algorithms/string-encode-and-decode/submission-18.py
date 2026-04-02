class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            n = int(s[i:j])
            i = j+1
            res.append(s[i:i+n])
            i += n

        return res
