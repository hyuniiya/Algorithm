def ticket():
    N = int(input())
    # 1차 티켓팅에서 팔린 티켓들 번호 리스트로 저장
    sold_tickets = list(map(int, input().split()))

    # 팔린 티켓 리스트 오름차순으로 정렬
    sold_tickets.sort()

    # 구매 가능한 가장 작은 번호 찾기
    ticket_number = 1
    for ticket in sold_tickets:
        if ticket != ticket_number:
            break
        ticket_number += 1

    print(ticket_number)
ticket()