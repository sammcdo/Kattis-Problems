number = input()

ans = ""
carry = 0

for n in number:
    n = int(n)
    n += 10 * carry

    ans += str(n//3)
    carry = n % 3

if carry > 0:
    carry = 1
    i = len(ans)-1
    while carry > 0:
        if i <= 0:
            i = 1
            ans = "0" + ans
        n = int(ans[i]) + carry
        ans = ans[0:i] + str(n % 10) + ans[i+1::]
        carry = n // 10
        i -= 1


while ans.startswith("0"):
    ans = ans[1::]

# print(ans, carry)

print(number)
print(ans)