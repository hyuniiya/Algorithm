def octopus_sequence():
    n = int(input())

    octopus = []
    for i in range(n):
        if i % 2 == 0:
            octopus.append(1)
        else:
            octopus.append(2)
    if n % 2 != 0:
        octopus[-1] = 3
    print(" ".join(map(str, octopus)))
octopus_sequence()