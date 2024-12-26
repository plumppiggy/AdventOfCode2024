input = ""
with open('input.txt') as f:
  for line in f.readlines():
    if line != '\n':
      input = line.strip()

mp = []
id = 0
for i in range(0, len(input)):
  for j in range(0, int(input[i])):
    if i % 2 == 0:
      mp.append(str(id))
    else:
      mp.append('.')

  if i % 2 == 0:
    id += 1

print(mp)

b = 0
e = len(mp) - 1

while b < e:
  if mp[b] == '.':
    while mp[e] == '.':
      e -= 1
    if e <= b:
      break

    mp[b] = mp[e]
    mp[e] = '.'
  b += 1

sum = 0
for idx, num in enumerate(mp):
  if num == '.':
    break

  sum += int(num) * idx

print(sum)
