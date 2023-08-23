maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_path(maze, start, end):
    queue = [start]
    visited = set()
    prev = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            path = []
            while current in prev:
                path.append(current)
                current = prev[current]
            path.append(start)
            return path[::-1]
        visited.add(current)
        for direction in directions:
            next_pos = (current[0] + direction[0], current[1] + direction[1])
            if next_pos[0] < 0 or next_pos[0] >= len(maze) or next_pos[1] < 0 or next_pos[1] >= len(maze[0]):
                continue
            if maze[next_pos[0]][next_pos[1]] == 1:
                continue
            if next_pos in visited:
                continue
            queue.append(next_pos)
            prev[next_pos] = current
    return None

path = find_path(maze, start, end)
if path:
    print("Путь найден:", path)
else:
    print("Путь не найден")