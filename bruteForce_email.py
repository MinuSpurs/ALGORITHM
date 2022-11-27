def bruteForce(p, t, k):
    M = len(p)
    N = len(t)
    i=k
    j=0
    while j<M and i<N:
        if t[i] != p[j]:
            i-=j
            j=-1
        i+=1
        j+=1
    if j==M:
        return i-M
    else:
        return i
    
fin = open('email.html', encoding='UTF-8')
text = fin.read()
pattern='mailto:'
pattern2='"'
M=len(pattern)
N=len(text)
K = 0
while True:
    pos = bruteForce(pattern, text, K)
    K=pos+M
    pos2= bruteForce(pattern2, text, K)
    K=pos2+M
    if K<N: 
        print(text[pos+7:pos2])
    else:
        break