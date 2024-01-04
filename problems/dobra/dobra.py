line = input()

newStr = ""
hasL1 = "L" in line
for char in line:
  if char == "_":
    newStr += "_"
  elif char in "AEIOU":
    newStr += "A"
  else:
    newStr += "B"

def poss(s, hasL):
  if "_" in s:
    combos = 0
    combos += 5*poss(s.replace("_", "A", 1), hasL) # Vowels
    combos += 20*poss(s.replace("_", "B", 1), hasL) # Consonents except L
    combos += 1*poss(s.replace("_", "B", 1), True) # Letter L
    return combos
  
  else:
    if hasL and "AAA" not in s and "BBB" not in s:
      return 1
    else:
      return 0
    
print(poss(newStr, hasL1))