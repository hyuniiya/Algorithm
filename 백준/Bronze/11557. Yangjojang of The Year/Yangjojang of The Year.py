def find_school():
    T = int(input())

    # 전체 테스트 케이스 수만큼 순회
    for t in range(T):
        school_list = []
        N = int(input())
        # 각 학교의 정보 입력 받아 리스트 추가
        for n in range(N):
            school, alcohol = input().split()
            school_list.append([school, int(alcohol)])
        # 학교 리스트를 술 소비량을 기준으로 정렬
        school_list.sort(key=lambda x: x[1])
        # 가장 많은 술을 소비한 학교의 이름 출력
        print(school_list[-1][0])
find_school()