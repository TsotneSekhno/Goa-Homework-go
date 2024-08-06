for x in "banana": #1
  print(x) 

cars = ["Bmw","Mersedes","Toyota"] #2
for c in cars:
   print(c)

names = ["sekhno", "gio", "mixo"]#3
for x in names:
  print(x) 
  if x == "sekhno":
    break

animals = ["tiger", "lion", "dog"]#4
for x in animals:
  if x == "lion":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]#5
for x in fruits:
  if x == "banana":
    continue
  print(x) 


for x in range(6):  #6
   print(x)


for x in range(6, 10):  #7
   print(x)


for x in range(2, 10, 4): #8
   print(x) 


for x in range(5):     #9
  print(x)
else:
  print("goa")


adj = ["red", "big", "tasty"]        #10
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
