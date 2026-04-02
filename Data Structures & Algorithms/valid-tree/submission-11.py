class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        V = [[] for _ in range(n)]
        visit = set()

        for edge in edges:
            V[edge[0]].append(edge[1])
            V[edge[1]].append(edge[0])


        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            
            for j in V[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True

        max_visit = 0
        for i in range(n):
            if not dfs(i, -1):
                return False

            max_visit = max(max_visit, len(visit))
            
            visit = set()
        return max_visit == n
