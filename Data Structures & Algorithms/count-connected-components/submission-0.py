class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, prev):
            if i in visit:
                return

            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                
                dfs(j, i)
            return
        
        num = 0
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                num += 1
        return num
            
        
