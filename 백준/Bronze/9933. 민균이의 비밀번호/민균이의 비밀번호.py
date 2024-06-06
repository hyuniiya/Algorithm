import sys

def find_password():
    input = sys.stdin.readline
    n = int(input())

    words = []
    for i in range (n):
        word = input().strip()
        words.append(word)

    for word in words:
        if word[::-1] in words:
            password_length = len(word)
            password_mid = word[password_length // 2]
            break
    print(password_length, password_mid)

find_password()