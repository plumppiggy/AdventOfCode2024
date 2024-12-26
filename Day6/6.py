from dataclasses import dataclass

@dataclass
class Direction:
  dx: int
  dy: int
  def turn_right(self):
    return Direction(self.dy, -self.dx)
  
  def __hash__(self) -> int:
    return hash((self.dx, self.dy))
  
  def __eq__(self, value: object) -> bool:
    return self.dx == value.dx and self.dy == value.dy

@dataclass
class Position:
  x: int
  y: int

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __hash__(self):
    return hash((self.x, self.y))
  
  def move(self, direction: Direction):
    return Position(self.x + direction.dx, self.y + direction.dy)

@dataclass
class Guard:
  direction: Direction
  position: Position

  def move_forward(self):
    return Guard(
      position=self.position.move(self.direction),
      direction=self.direction
    )
  
  def turn_right(self):
    return Guard(
      position=self.position,
      direction=self.direction.turn_right()
    )
  
  def __eq__(self, value: object) -> bool:
    return self.direction == value.direction and self.position == value.position
  
  def __hash__(self) -> int:
    return hash((self.direction, self.position))

def get_guard_pos(positions : list[list[str]]):
  position = Position(-1, -1)
  for i, line in enumerate(positions):
    for j, char in enumerate(line):
      if char == "^":
        position.x = i
        position.y = j

  return position

positions = []
with open('input.txt') as file:
  for line in file.readlines():
    positions.append(list(line.strip()))

print(positions)

n = len(positions)
m = len(positions[0])



def is_looped(positions, guard):

  vis = set()
  while True:
    if guard in vis:
      return True
    
    vis.add(guard)
    next_g = guard.move_forward()

    if not (0 <= next_g.position.x < n and 0 < next_g.position.y < m):
      return False

    if positions[next_g.position.x][next_g.position.y] == '#':
      next_g = guard.turn_right()

    guard = next_g

loops = 0

curr_g = Guard(
  position=get_guard_pos(positions),
  direction=Direction(dx=-1, dy=0)
)

for i, line in enumerate(positions):
  for j, char in enumerate(line):
    if char != '.':
      continue

    positions[i][j] = '#'

    if is_looped(positions, curr_g):
      loops += 1

    positions[i][j] = '.'

print(f"loops {loops}")




