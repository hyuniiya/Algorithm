def reverse_constant():
    A, B = input().split()

    A_reversed = int(A[::-1])
    B_reversed = int(B[::-1])

    print(max(A_reversed, B_reversed))
    
reverse_constant()