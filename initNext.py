def initNext(p,m):
    m = len(p)
    next[0] = -1
    i=0
    j=-1
    while i<m:
        next[i]=j
        while j>=0 and p[i] != p[j]:
            j=next[j]
        i+=1
        j+=1

next = [0]*50
pattern='abracadabra'
m=len(pattern)
initNext(pattern,m)
for i in range(1,m):
    print(next[i], end=' ')