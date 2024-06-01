def print_in_chunks():
    word = input()
    length = len(word)  
    
    for i in range(0, length, 10):
        print(word[i:i+10])

print_in_chunks()