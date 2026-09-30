# DFS Maze Solving using User Input

def dfs_maze(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    # Stack for DFS
    stack = [start]

    # Set to store visited cells
    visited = set()

    # Dictionary to store parent of each cell
    parent = {}

    visited.add(start)

    # Up, Down, Left, Right
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    while stack:

        # Remove last element from stack
        current = stack.pop()

        # Check if goal is reached
        if current == goal:

            path = []

            # Reconstruct path
            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)

            # Reverse path
            path.reverse()

            return path

        r, c = current

        # Check all four directions
        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            # Check boundary
            if 0 <= nr < rows and 0 <= nc < cols:

                # Check open cell and not visited
                if maze[nr][nc] == 0 and (nr, nc) not in visited:

                    visited.add((nr, nc))

                    # Store parent
                    parent[(nr, nc)] = current

                    # Add to stack
                    stack.append((nr, nc))

    return None


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("DFS Maze Solving")
print("----------------")

# Number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter maze:")
print("0 = Open path")
print("1 = Wall")

maze = []

for i in range(rows):
    while True:
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        if len(row) == cols and all(x in [0, 1] for x in row):
            maze.append(row)
            break
        else:
            print("Invalid input! Enter exactly", cols,
                  "values containing only 0 or 1.")

# Start position
print("\nEnter Start position")
start_row = int(input("Enter start row: "))
start_col = int(input("Enter start column: "))

start = (start_row, start_col)

# Goal position
print("\nEnter Goal position")
goal_row = int(input("Enter goal row: "))
goal_col = int(input("Enter goal column: "))

goal = (goal_row, goal_col)

# Check start and goal
if maze[start_row][start_col] == 1:
    print("Start position is a wall!")
elif maze[goal_row][goal_col] == 1:
    print("Goal position is a wall!")
else:

    # Call DFS function
    path = dfs_maze(maze, start, goal)

    if path:

        print("\nDFS Path Found:")
        print(path)

        # Create a copy of maze
        result = [row[:] for row in maze]

        # Mark path
        for r, c in path:
            result[r][c] = '*'

        # Mark Start and Goal
        result[start_row][start_col] = 'S'
        result[goal_row][goal_col] = 'G'

        print("\nMaze with DFS Path:")
        for row in result:
            print(" ".join(map(str, row)))

        print("\nPath Cost:", len(path) - 1)

    else:
        print("\nNo path found!")