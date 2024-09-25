from collections import deque

def solution(progresses, speeds):
    queue = deque([(p, s) for p, s in zip(progresses, speeds)])
    answer = []
    day = 0
    count = 0

    while queue:
        if (queue[0][0] + day * queue[0][1]) >= 100:
            queue.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            else:
                day += 1

    answer.append(count)
    return answer