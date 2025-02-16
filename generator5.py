def gen(N):
    for i in range(N+1):
        yield str(N-i)
n=int(input())
print(",".join(gen(n)))