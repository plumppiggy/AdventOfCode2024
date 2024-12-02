levels = []

with open('input.txt', 'r') as file:
  for line in file:
    nums = [int(x) for x in line.split(' ')]
    levels.append(nums)

def is_safe(nums: list[int]):
  increasing = False
  for i in range(0, len(nums)):
    if i == 0 and i + 1 < len(nums):
      if nums[0] < nums[1]:
        increasing = True
      elif nums[0] == nums[1]:
        return False

      continue

    if increasing:
      diff = nums[i] - nums[i-1]

    else:
      diff = nums[i-1] - nums[i]
    if diff <= 0 or diff > 3:
      return False
  return True

safe = 0
non_safe = []
for level in levels:
  if is_safe(level):
    safe += 1
  else:
    non_safe.append(level)

for level in non_safe:
  for i in range(len(level)):
    report = level[:i] + level[i + 1:]
    if is_safe(report):
      safe += 1
      break

print(safe)
    
    




