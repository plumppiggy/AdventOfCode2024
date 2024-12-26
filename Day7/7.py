from itertools import product
OPERATIONS = {
  '+': lambda x,y : x + y,
  '*': lambda x,y : x * y,
  '||': lambda x,y: int(str(x) + str(y))
}

equations = []

with open('input.txt') as file:
  for line in file.readlines():
    ans, exp = line.split(': ')
    ans = int(ans)
    exp = [int(x) for x in exp.split()]

    equations.append((ans, exp))

s = 0

for ans, exp in equations:
  for operations in product(OPERATIONS.keys(), repeat=len(exp) - 1):
    pos_a = exp[0]

    for i, operation in enumerate(operations, start=1):
      pos_a = OPERATIONS[operation](pos_a, exp[i])

      if pos_a > ans:
        break

    if pos_a == ans:
      s += ans
      break

print(s)