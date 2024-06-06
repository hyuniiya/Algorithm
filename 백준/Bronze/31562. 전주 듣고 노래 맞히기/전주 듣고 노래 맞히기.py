import sys

def find_music():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    music = {}

    for n in range(N):
        music_note = input().split()
        S = music_note[1]
        sounds = music_note[2:9]  # 7개의 음이름을 리스트로 저장
        music[S] = sounds[:3]     # 첫 세 음만 저장

    for m in range(M):
        three_sounds = input().split()
        matching_music = []

        for title, sounds in music.items():
            if three_sounds == sounds:  # 첫 세 음이 일치하는지 확인
                matching_music.append(title)

        if len(matching_music) == 0:
            print("!")  # 일치하는 노래가 없을 때
        elif len(matching_music) == 1:
            print(matching_music[0])  # 정확히 하나의 노래가 일치할 때
        else:
            print("?")  # 여러 노래가 일치할 때

find_music()