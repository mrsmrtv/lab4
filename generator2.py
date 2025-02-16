def gen(N):
    for i in range(0,N+1,2):
        yield str(i)
n=int(input())
print(", ".join(gen(n)))