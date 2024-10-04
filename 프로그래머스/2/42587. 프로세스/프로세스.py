def solution(priorities, location):
    processes = list(enumerate(priorities))
    execution_order = 0

    while processes:
        max_priority = max(p for _, p in processes)
        
        current = processes.pop(0)
        
        if current[1] == max_priority:
            execution_order += 1
            if current[0] == location:
                return execution_order
        else:
            processes.append(current)

    return -1