levels = []

with open('input.txt', 'r') as file:
  for line in file:
    nums = [int(x) for x in line.split(' ')]
    levels.append(nums)

def is_safe(nums: list[int]):
  increasing = False
  for i in range(0, len(level)):
    if i == 0 and i + 1 < len(level):
      if level[0] < level[1]:
        increasing = True
      elif level[0] == level[1]:
        return False

      continue

    if increasing:
      diff = level[i] - level[i-1]

    else:
      diff = level[i-1] - level[i]
    if diff <= 0 or diff > 3:
      return False
  return True

safe = 0
for level in levels:
  if is_safe(level):
    safe += 1
  

print(safe)    
    
    




