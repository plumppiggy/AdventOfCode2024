from collections import defaultdict

rules = defaultdict(set)
updates = []
input = ""
with open('input.txt', 'r') as file:
  for line in file.readlines():
    input += line

  print(input)

  page_rules, pages = input.split('\n\n')

  for rule in page_rules.split('\n'):
    print(rule)
    l, r = map(int, rule.split('|'))
    rules[l].add(r)

  for page in pages.split('\n'):
    updates.append(list(map(int, page.split(','))))

ans = 0
ans_2 = 0
def top_sort(nodes, graph):
  def dfs(u):
    vis.add(u)

    for v in graph[u]:
      if v in vis:
        continue
      if v not in graph:
        continue
      if v not in nodes:
        continue
      yield from dfs(v)

    yield u

  stack = []
  vis = set()

  for node in nodes:
    if node in vis:
      continue
    for other in dfs(node):
      stack.append(other)

  return stack

for update in updates:
  is_valid = True
  seen = set()

  for page in update:
    if rules[page] & seen:
      is_valid = False
    seen.add(page)

  if not is_valid:
    update = top_sort(set(update), rules)
    ans_2 += update[len(update) // 2]

print(ans)
print(ans_2)





