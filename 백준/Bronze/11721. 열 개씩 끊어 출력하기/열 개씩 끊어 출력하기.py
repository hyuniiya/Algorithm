def print_in_chunks():
    word = input() 
    chunks = [word[i:i+10] for i in range(0, len(word), 10)]
    for chunk in chunks:
        print(chunk)

print_in_chunks()