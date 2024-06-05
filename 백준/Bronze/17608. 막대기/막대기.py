import sys
def bar():
    input = sys.stdin.readline
    n = int(input())
    # 막대기 높이 저장할 리스트
    stacks = []
    # 높이 리스트 추가
    for i in range(n):
        h = int(input())
        stacks.append(h)
    # 보이는 막대기 높이 저장할 리스트
    stack = []
    # 리스트를 역순으로 순회하며 추가하기
    for h in stacks[::-1]:
        # 처음 스택이 비어 있는 상태이거나, 막대기 높이가 스택에 쌓인 수보다 클 경우
        if not stack or h > stack [-1]:
            stack.append(h)
    # 막대기 개수 반환
    print(len(stack))

bar()