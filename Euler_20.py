def f(n):
    if (n==1): return 1
    else: return n*f(n-1)
print (sum([int (i) for i in [i for i in str(f(100))]]))
