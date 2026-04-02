class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        V = [[] for _ in range(n)]
        visit = defaultdict(int)

        for edge in edges:
            V[edge[0]].append(edge[1])
            V[edge[1]].append(edge[0])


        def dfs(i, prev):
            if visit[i] > 1:
                return False
            
            visit[i] += 1
            
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
            
            visit = defaultdict(int)
        return max_visit == n
