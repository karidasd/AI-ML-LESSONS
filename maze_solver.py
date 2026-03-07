from collections import deque

# Ο λαβύρινθος: 0 = δρόμος, 1 = τοίχος, S = Αρχή, E = Έξοδος
maze = [
    ["S", 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, "E"]
]

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        curr_r, curr_c = queue.popleft()

        if maze[curr_r][curr_c] == "E":
            return "Βρέθηκε η έξοδος!"

        # Κινήσεις: Πάνω, Κάτω, Αριστερά, Δεξιά
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = curr_r + dr, curr_c + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != 1 and (r, c) not in visited:
                visited.add((r, c))
                queue.append((r, c))
                parent[(r, c)] = (curr_r, curr_c)
    
    return "Δεν υπάρχει μονοπάτι."

print(solve_maze(maze))
