a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

xm,xy = min(set([a[0],b[0],c[0]])),max(set([a[0],b[0],c[0]]))
ym,yy = min(set([a[1],b[1],c[1]])),max(set([a[1],b[1],c[1]]))
opts  = [[xm,ym], [xy,ym],[xm,yy],[xy,yy]]

for i in opts:
    if i not in [a,b,c]:
        print(*i)
        exit()