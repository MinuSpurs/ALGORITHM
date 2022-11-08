def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c) - 64

def initSkip(p):
    M=len(p)
    NUM = 27
    skip=[0] * NUM
    for i in range(NUM):
        skip[i]=M
    for i in range(M):
        skip[index(p[i])]=M-i-1
