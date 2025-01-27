w=input
x=range
p=print
y=int
n,k,r=[y(i)for i in w().split()]
d=[y(i)for i in w().split()]
c={}
t={}
m=set()
for i in x(n):
    c[i]=0
    t[i]=0
for i in x(r):
    a,b=[y(i)for i in w().split()]
    t[a]=b
s=0
l=n+1
for i in x(0,len(d)):
    c[d[i]]+=1
    if c[d[i]]>=t[d[i]]and t[d[i]]!=0:
        m.add(d[i])
    if len(m)==r:
        while c[d[s]]> t[d[s]]or t[d[s]]==0:
            if c[d[s]]>t[d[s]]:
                c[d[s]]-=1
            s+=1
        z=i-s+1
        if z