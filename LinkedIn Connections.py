n, m = int(input()), int(input())
adj = [[] for _ in range(n + 2)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
s = int(input())
vis, dis = [0 for _ in range(n + 1)], [float('inf') for _ in range(n + 1)]
vis[s], dis[s], qu = 1, 0, [s]
while (qu):
    par = qu.pop()
    for i in adj[par]:
        if (not vis[i]):
            vis[i] = 1; qu.append(i); dis[i] = dis[par] + 1
print("\n".join(["no" if (dis[int(input())] > 3) else "yes" for _ in range(int(input()))]))