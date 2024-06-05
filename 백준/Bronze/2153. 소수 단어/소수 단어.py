import string

n = input()
alphabet = list(string.ascii_letters)
total = 0
for char in n:
    index = alphabet.index(char) + 1
    total += index
def find_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
        	return 'It is not a prime word.'
    return 'It is a prime word.'
print(find_prime(total))