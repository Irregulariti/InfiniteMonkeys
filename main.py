for _ in range(int(input())):
    n = int(input())
    portals = [[int(i) for i in input().split()] for __ in range(n)]
    q = int(input())
    X = [int(x) for x in input().split()]

    portals += [[x] * 4 for x in X]

    portals.sort(key=lambda i: -i[3])

    j = 0
    qans = {}
    for l, r, a, b in portals:
        while b < portals[j][0]:
            j += 1
        qans[b] = qans.get(portals[j][3], b)

    print(*[qans[x] for x in X])
