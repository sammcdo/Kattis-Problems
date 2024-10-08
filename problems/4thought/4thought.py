ops = ["*", "+", "-", "//"]

convert = {
  "*": lambda x,y: x*y,
  "+": lambda x,y: x+y,
  "-": lambda x,y: x-y,
  "/": lambda x,y: x//y
}

pre = {}

for i in range(4):
  opA = ops[i]
  for j in range(4):
    opB = ops[j]
    for k in range(4):
      opC = ops[k]

      this = eval(f"4{opA}4{opB}4{opC}4")
      pre[this] = f"4 {opA} 4 {opB} 4 {opC} 4 = {this}"
      pre[this] = pre[this].replace("//", "/")

n = int(input())

for i in range(n):
  x = int(input())
  if x in pre:
    print(pre[x])
  else:
    print("no solution")
