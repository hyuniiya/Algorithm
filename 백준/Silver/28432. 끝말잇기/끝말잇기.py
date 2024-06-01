def find_word():
    N = int(input())
    word = [input() for _ in range(N)]

    M = int(input())
    candidates = [input() for _ in range(M)]

    question_i = word.index('?')
    prev_word = word[question_i - 1] if question_i > 0 else ''
    next_word = word[question_i + 1] if question_i < N - 1 else ''

    for candidate in candidates:
        if candidate in word:  # 후보 단어가 이미 끝말잇기 기록에 있는 경우
            continue
        
        # 끝말잇기 규칙을 만족하면서 중복되지 않는 단어인지 확인
        if (not prev_word or candidate[0] == prev_word[-1]) and (not next_word or candidate[-1] == next_word[0]):
            print(candidate)
            return

find_word()