class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            j = i
            while s[i] != '#':
                i += 1
            n = int(s[j:i])
            i += 1
            res.append(s[i:i+n])
            i += n

        return res
