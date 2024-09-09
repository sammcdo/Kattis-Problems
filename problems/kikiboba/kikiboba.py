a=input()
b,k=a.count('b'),a.count('k')
print("none" if b==0 and k==0 else "boba" if b>k else "kiki" if b<k else "boki")