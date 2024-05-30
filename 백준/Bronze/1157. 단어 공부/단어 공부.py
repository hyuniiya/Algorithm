# 대문자로 변환
# 알파벳, 개수 딕셔너리에 저장하기
# 빈도수 높은 순으로 2개 출력
# 빈도수 높은 2개 비교후 같을 경우, '?' 출력
# 다를 경우, 첫번째 최대 빈도수 출력
## 만약 하나일 경우, 최대 빈도수 출력 추가
from collections import Counter

def find_most_word():
    words = input().upper()

    alphabet = Counter(words)

    most_common_alphabet = alphabet.most_common(2)

    if len(most_common_alphabet) == 1:
        print(most_common_alphabet[0][0])
    elif most_common_alphabet[0][1] == most_common_alphabet[1][1]:
        print('?')
    else:
        print(most_common_alphabet[0][0])

find_most_word()