nums_1, nums_2 = [], []

with open('input.txt', 'r') as file:
  for line in file:
    nums = [int(x) for x in line.strip().split(' ') if x != '']
    nums_1.append(nums[0])
    nums_2.append(nums[1])

nums_1.sort()
nums_2.sort()

ans = 0
for k, l in zip(nums_1, nums_2):
  ans += abs(l -k)

print(ans)