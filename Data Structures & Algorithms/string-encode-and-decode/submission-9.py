class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += f'{len(s)}#{s}'
        return ans

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            inner_str = ''
            n_str = ''

            while (s[i] != '#'):
                n_str += s[i]
                i+=1
            
            n = int(n_str)
            i+=1

            for _ in range(n):
                inner_str += s[i]
                i += 1
            strs.append(inner_str)
        return strs


