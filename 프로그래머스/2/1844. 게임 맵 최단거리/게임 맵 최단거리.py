def solution(maps):
    n, m = len(maps), len(maps[0])
    
    current_positions = [(0, 0)]
    
    steps = 0
    
    while current_positions:
        steps += 1
        next_positions = []
        
        for x, y in current_positions:
            if x == n - 1 and y == m - 1:
                return steps
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    next_positions.append((nx, ny))
                    maps[nx][ny] = 0
        
        current_positions = next_positions
    
    return -1