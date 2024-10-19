def solution(maps):
    rows, cols = len(maps), len(maps[0])
    
    current_positions = [(0, 0)]
    
    steps = 0
    
    while current_positions:
        steps += 1
        next_positions = []
        
        for x, y in current_positions:
            if x == rows - 1 and y == cols - 1:
                return steps
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < rows and 0 <= new_y < cols and maps[new_x][new_y] == 1:
                    next_positions.append((new_x, new_y))
                    maps[new_x][new_y] = 0
        
        current_positions = next_positions
    
    return -1