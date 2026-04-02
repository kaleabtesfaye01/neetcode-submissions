class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            n_str = ''
            while s[i] != '#':
                n_str += s[i]
                i += 1
            i += 1
            n = int(n_str)
            my_str = ''
            for j in range(i, i+n):
                my_str += s[j]
            res.append(my_str)
            i += n
        return res








