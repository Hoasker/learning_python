M = input()
N = input()
F = [[0]*(N+1) for i in range(M+1)]

for i in range(1, N+1):
    for k in range(1, M+1):
        if M[i] <= k:
            F[k][i] = max(N[i]+F[k-M[i]][i-1], F[k][i-1])
        else:
            F[k][i] = F[k][i-1]
    # F[M][N] <- Answer