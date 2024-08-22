import bisect

a = int(input())

connections = [int(input()) for i in range(a)]

def lis(arr):
    n = len(arr)
    ans = [arr[0]]

    for i in range(1, n):
        if arr[i] > ans[-1]:
            ans.append(arr[i])
        else:
            x = bisect.bisect_left(ans, arr[i])
            ans[x] = arr[i]
    
    return len(ans)

ans = lis(connections)

print(ans)