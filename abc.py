N = int(input())
ans = 0

for i in range(1, N//2 + 1):
    if i != N-i:
        cou = set()
        n = 1
        while n <= N**(1/2):
            if i % n == 0:
                cou.add(n)
                cou.add(i//n)
            n += 1

        cou_ = set()
        n = 1
        while n <= N**(1/2):
            if (N-i) % n == 0:
                cou_.add(n)
                cou_.add((N-i)//n)
            n += 1

        ans += len(cou)*len(cou_)*2  
        print(i, cou, cou_)  
    else:
        cou = set()
        n = 1
        while n <= N**(1/2):
            if (N-i) % n == 0:
                cou.add(n)
                cou.add(i//n)
            n += 1

        ans += len(cou)*2
        print(i, cou)

print(ans)