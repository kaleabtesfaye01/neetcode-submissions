class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += f'{len(s)}k{s}'
            # len(s) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            n_str = []

            while (s[i] != 'k'):
                n_str.append(s[i])
                i += 1
            
            myStr = ''.join(n_str)

            strs.append(s[i+1:i+int(myStr)+1])

            i = i + 1 + int(myStr)
        
        return strs
