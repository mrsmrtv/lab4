def gen(N):
    for i in range(0,N+1):
        if i%3==0 and i%4==0:
            yield str(i)
n=int(input())
print(",".join(gen(n)))