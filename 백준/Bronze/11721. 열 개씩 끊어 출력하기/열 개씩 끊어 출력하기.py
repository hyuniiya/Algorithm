# 문자열 10개씩 wrapping하기
import textwrap

def wrap_text():
    word = input() 
    print('\n'.join(textwrap.wrap(word, 10)))

wrap_text()