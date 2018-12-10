from random import randint

def build_maze(m,n,swag):
  grid = []
  for i in range(m):
    row = []
    for j in range(n):
      row.append('wall')
    grid.append(row)
  start_i = randint(0, m-1)
  start_j = randint(0, n-1)
  grid[start_i][start_j] = 'start'
  mow(grid, start_i, start_j)
  explore_maze(grid, start_i, start_j, swag)
  return grid

def print_maze(grid):
  for row in grid:
    printable_row = ''
    for cell in row:
      if cell == 'wall':
        char = '|'
      elif cell == 'empty':
        char = ' '
      else:
        char = cell[0]
      printable_row += char
    print(printable_row)

def mow(grid, i, j):
    directions = ['U', 'D', 'L', 'R']
    while len(directions) > 0:
        directions_index = randint(0, len(directions) - 1)
        direction = directions.pop(directions_index)
        if direction == 'U':
            if i -2 <= 0:
                continue
            elif grid[i-2][j] == 'wall':
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j)
        elif direction == 'D':
            if i + 2 >= len(grid):
                continue
            elif grid[i + 2][j] == 'wall':
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j)
        elif direction == 'L':
            if j - 2 <= 0:
                continue
            elif grid[i][j -2] == 'wall':
                grid[i][j - 1] = 'empty'
                grid[i][j - 2] = 'empty'
                mow(grid, i, j-2)
        elif direction == 'R':
            if j + 2 >= len(grid[0]):
                continue
            elif grid[i][j +2] == 'wall':
                grid[i][j + 1] = 'empty'
                grid[i][j + 2] = 'empty'
                mow(grid, i, j + 2)
                
def explore_maze(grid, start_i, start_j, swag):
    grid_copy = [row[:] for row in grid]
    bfs_queue = [[start_i, start_j]]
    directions = ['U', 'D', 'L', 'R']
    while bfs_queue:
        i, j = bfs_queue.pop(0)
        if grid[i][j] != 'start' and randint(1,10) == 1:
            grid[i][j] = swag[randint(0,len(swag) - 1)]
        grid_copy[i][j] = 'visited'
        for direction in directions:
            explore_i, explore_j = i, j
            if direction == 'U':
                explore_i = i - 1
            elif direction == 'D':
                explore_i = i + 1
            elif direction == 'L':
                explore_j = j - 1
            else:
                explore_j = j + 1
            if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
                continue
            elif grid_copy[explore_i][explore_j] != 'wall' and grid_copy[explore_i][explore_j] != 'visited':
                bfs_queue.append([explore_i,explore_j])
    grid[i][j] = 'end'

print(print_maze(build_maze(20,30,['candy corn', 'werewolf', 'pumpkin'])))

def build_maze_more(m,n,swag):
  grid = []
  for i in range(m):
    row = []
    for j in range(n):
      row.append('wall')
    grid.append(row)
  start_i = randint(0, m-1)
  start_j = randint(0, n-1)
  grid[start_i][start_j] = 'start'
  mow_more(grid, start_i, start_j)
  explore_maze(grid, start_i, start_j, swag)
  return grid

def mow_more(grid, i, j):
    directions = ['U', 'D', 'L', 'R']
    move_num = 4
    while len(directions) > 0:
        directions_index = randint(0, len(directions) - 1)
        direction = directions.pop(directions_index)        
        if direction == 'U':
            if i - move_num <= 0:
                continue
            elif grid[i - move_num][j] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i - n][j] = 'empty'
                mow_more(grid, i - move_num, j)
        elif direction == 'D':
            if i + move_num >= len(grid):
                continue
            elif grid[i + move_num][j] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i + n][j] = 'empty'
                mow_more(grid, i + move_num, j)
        elif direction == 'L':
            if j - move_num <= 0:
                continue
            elif grid[i][j -move_num] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i][j - n] = 'empty'
                mow_more(grid, i, j - move_num)
        elif direction == 'R':
            if j + move_num >= len(grid[0]):
                continue
            elif grid[i][j + move_num] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i][j + n] = 'empty'
                mow_more(grid, i, j + move_num)


print(print_maze(build_maze_more(20,30,['candy corn', 'werewolf', 'pumpkin'])))

def build_maze_rand(m,n,swag):
  grid = []
  for i in range(m):
    row = []
    for j in range(n):
      row.append('wall')
    grid.append(row)
  start_i = randint(0, m-1)
  start_j = randint(0, n-1)
  grid[start_i][start_j] = 'start'
  mow_rand(grid, start_i, start_j)
  #explore_maze(grid, start_i, start_j, swag)
  return grid

def mow_rand(grid, i, j):
    directions = ['U', 'D', 'L', 'R']
    move_num = randint(3,5)
    while len(directions) > 0:
        directions_index = randint(0, len(directions) - 1)
        direction = directions.pop(directions_index)        
        if direction == 'U':
            if i - move_num <= 0:
                continue
            elif grid[i - move_num][j] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i - n][j] = 'empty'
                mow_rand(grid, i - move_num, j)
        elif direction == 'D':
            if i + move_num >= len(grid):
                continue
            elif grid[i + move_num][j] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i + n][j] = 'empty'
                mow_rand(grid, i + move_num, j)
        elif direction == 'L':
            if j - move_num <= 0:
                continue
            elif grid[i][j -move_num] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i][j - n] = 'empty'
                mow_rand(grid, i, j - move_num)
        elif direction == 'R':
            if j + move_num >= len(grid[0]):
                continue
            elif grid[i][j + move_num] == 'wall':
                for n in range(1, move_num + 1):
                    grid[i][j + n] = 'empty'
                mow_rand(grid, i, j + move_num)

print(print_maze(build_maze_rand(20,30,['candy corn', 'werewolf', 'pumpkin'])))