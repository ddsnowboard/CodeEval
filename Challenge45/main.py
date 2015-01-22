from sys import argv
with open(argv[1], 'r') as f:
    times = []
    for i in f:
        n = int(i)
        count = 0
        while str(n) != str(n)[::-1]:
            n += int(str(n)[::-1])
            count += 1
        times.append((count, n))
    print("\n".join([str(i[0])+" "+str(i[1]) for i in times]))