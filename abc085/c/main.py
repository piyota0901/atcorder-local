N, Y = map(int,input().split())
ares,bres,cres = -1,-1,-1

for x in range(N+1): # 0スタートだから
    for y in range(N+1):
        z = N - y - x

        if z < 0 or z > N:
            continue

        if (10000*x + 5000*y + 1000*z) == Y:
            ares,bres,cres = x,y,z

print(ares,bres,cres)