def gen(N):
    for i in range(1,N+1):
        yield i**2
n=int(input("Num: "))
for ans in gen(n):
    print(ans)