#Python While Loops


i = 1
while i < 100:
  print(i)
  i += 1


i = 0
while i < 20:
  i += 1
  if i == 7:
    continue
  print(i)


i = 1
while i < 21:
  print(i)
  if i == 6:
    break
  i += 3