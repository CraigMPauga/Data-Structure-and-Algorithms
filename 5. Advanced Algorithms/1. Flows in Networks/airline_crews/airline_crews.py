# python3

from collections import deque

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def read_data_test(self):

        lines=open("tests/01",'r').readlines()
        n,m = map(int, lines[0].split())
        adj_matrix = []
        for i in range(1,len(lines)):
            adj_matrix.append(list(map(int,lines[i].split())))
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching_naive(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
                    matching[i] = j
                    busy_right[j] = True
        return matching

    def find_matching(self,adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        num_vertex = n+m+2
        capacity_matrix = [[0 for k in range(num_vertex)] for i in range(num_vertex)]

        for u in range(1,n+1):
            capacity_matrix[0][u] = 1

        for u in range(n+1,n+m+1):
            capacity_matrix[u][n+m+1] = 1
        
        for u in range(n):
            for v in range(m):
                cap = adj_matrix[u][v]
                capacity_matrix[u+1][v+n+1] = cap
        matches = self.max_flow(num_vertex ,0, (n+m+1), capacity_matrix)
        line=[]
        for m in range(1,n+1):
            if m in matches:
                line.append(str(matches[m]-n))
            else:
                line.append(str(-1))
        print(' '.join(line))
            


    def max_flow(self,n,s,t,c):
        INF = float("Inf")
        max_flow = 0
        ans=dict()
        f = [[0 for k in range(n)] for i in range(n)]

        while True:
            prev = [-1 for _ in range(n)]
            prev[s] = -2
            q = deque()
            q.append(s)

            while q and prev[t]==-1:
                u = q.popleft()
                for v in range(n):
                    cf =c[u][v] - f[u][v]
                    if cf > 0 and prev[v]==-1:
                        q.append(v)
                        prev[v] = u

            if prev[t]==-1:
                break

            v = t
            delta = INF
            while True:
                u=prev[v]
                cf = c[u][v] - f[u][v]
                delta = min(delta, cf)
                v = u
                if v==s:
                    break

            v = t
            while True:
                u = prev[v]
                f[u][v]+=delta
                f[v][u]-=delta
                if u!=s and v!=t:
                    ans.setdefault(u,v)
                v=u
                if v==s:
                    break

            max_flow+=delta

        return ans

    def solve(self):
        adj_matrix = self.read_data()
        #adj_matrix = self.read_data_test()
        matching = self.find_matching(adj_matrix)
        #self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
