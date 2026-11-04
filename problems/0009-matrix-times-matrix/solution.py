def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m = len(a)
    n = len(a[0])
    p = len(b[0])

    if len(b) != n:
        return -1

    c = [[0]*p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            s = 0
            for k in range(n):
                s += a[i][k] * b[k][j]
            c[i][j] = s
	
    return c