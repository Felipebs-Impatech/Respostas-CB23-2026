def bfs(maze, wall, cheese):
    m, n = len(maze), len(maze[0])
    start = (1, 1)  # Começando do canto superior esquerdo do labirinto
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        x, y = queue.pop(0)

        if maze[x][y] == cheese:
            # Reconstruindo o caminho quando encontra o queijo
            path = []
            pos = (x, y)
            while pos is not None:
                path.append(pos)
                pos = parent[pos]
            return path[::-1]  # Retorna o caminho do início ao queijo

        # Explorando casas adjacentes
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != wall and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return None  # Retorna None se não encontrar caminho, não é necessário, pois o labirinto é perfeito, mas pode ser útil

# função que pega o caminho e imprime o labirinto com o caminho marcado
def print_maze_with_path(maze, path):
    maze_with_path = [row[:] for row in maze]  # Faz uma cópia do labirinto original
    for x, y in path:
        if maze_with_path[x][y] == ' ':
            maze_with_path[x][y] = '*'  
    for row in maze_with_path:
        print(" ".join(map(str, row)))