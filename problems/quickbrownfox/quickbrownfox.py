for i in range(int(input())):
    x=set(chr(i)for i in range(97,123))-set(input().lower())
    print("pangram"if len(x)==0 else "missing "+"".join(sorted(list(x))))