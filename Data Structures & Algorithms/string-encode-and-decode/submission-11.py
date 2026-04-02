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
            n_str = ''

            while (s[i] != '#'):
                n_str += s[i]
                i += 1

            strs.append(s[i+1:i+int(n_str)+1])

            i = i + int(n_str) + 1
        
        return strs


