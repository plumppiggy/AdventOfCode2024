from collections import defaultdict

arr = []
with open('input.txt') as f:
  for line in f.readlines():
    arr.append(list(line.strip()))

print(arr)

mp = defaultdict(list)
n, m = len(arr), len(arr[0])

for i in range(n):
  for j in range(m):
    if arr[i][j] != '.':
      mp[arr[i][j]].append((i, j))

ans = set()
for i in mp:
  tmp = mp[i]
  x = len(tmp)
  ans.update(tmp)

  for j in range(x-1):
    for k in range(j+1, x):
      diff = (tmp[j][0] - tmp[k][0], tmp[j][1] - tmp[k][1])
      p1 = (tmp[j][0] + diff[0], tmp[j][1] + diff[1])
      while -1 < p1[0] < n and -1 < p1[1] < m:
        ans.add(p1)
        p1 = (p1[0] + diff[0], p1[1] + diff[1])
      p2 = (tmp[k][0] - diff[0], tmp[k][1] - diff[1])
      while -1 < p2[0] < n and -1 < p2[1] < m:
        ans.add(p2)
        p2 = (p2[0] - diff[0], p2[1] - diff[1])

print(len(ans))



