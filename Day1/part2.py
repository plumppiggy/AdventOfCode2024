from collections import Counter
nums_1, nums_2 = [], []

with open('input.txt', 'r') as file:
  for line in file:
    nums = [int(x) for x in line.strip().split(' ') if x != '']
    nums_1.append(nums[0])
    nums_2.append(nums[1])

c = Counter(nums_2)

ans = 0
for num in nums_1:
  if num in c:
    ans += num * c[num]


print(ans)