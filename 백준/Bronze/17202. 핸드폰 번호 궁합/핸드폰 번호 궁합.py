def phone_number():
    A = input()
    B = input()

    number_list =[]
    for a, b in zip(A, B):
        number_list.append(int(a))
        number_list.append(int(b))

    for length in range(15, 1, -1):
        for i in range(length):
            number_list[i] = int(str(number_list[i] + number_list[i + 1])[-1])

    return f"{number_list[0]}{number_list[1]}"

print(phone_number())