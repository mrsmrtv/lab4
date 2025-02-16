def gen(a,b):
    for i in range(a,b+1):
        yield str(i**2)
A=int(input())
B=int(input())
print(",".join(gen(A,B)))