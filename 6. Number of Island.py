N = int(input())
M = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

def get_shape(r, c):
    shape = []
    stack = [(r, c)]
    visited[r][c] = True
    while stack:
        curr_r, curr_c = stack.pop()
        shape.append((curr_r, curr_c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = True
                stack.append((nr, nc))
    return shape

def normalize(shape):
    all_versions = []
    for x_sign, y_sign, swap in [
        (1, 1, False), (1, -1, False), (-1, 1, False), (-1, -1, False),
        (1, 1, True), (1, -1, True), (-1, 1, True), (-1, -1, True)
    ]:
        temp = []
        for r, c in shape:
            curr_r, curr_c = (c, r) if swap else (r, c)
            temp.append((curr_r * x_sign, curr_c * y_sign))

        min_r = min(r for r, c in temp)
        min_c = min(c for r, c in temp)
        version = sorted([(r - min_r, c - min_c) for r, c in temp])
        all_versions.append(tuple(version))
    return min(all_versions)
unique_islands = set()
for r in range(N):
    for c in range(M):
        if grid[r][c] == 1 and not visited[r][c]:
            island_coords = get_shape(r, c)
            island_signature = normalize(island_coords)
            unique_islands.add(island_signature)

print(len(unique_islands))