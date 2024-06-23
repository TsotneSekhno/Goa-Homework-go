def my_function():              #1
  print("goa is the best")

my_function()



def my_function(name):        #2
  print(name + " is good boy")

my_function("wiki")
my_function("Tobias")
my_function("zuka")


def my_function(name, lname):    #3
  print(name + " " + lname)

my_function("email","refsnes")


def my_function(*kids):         #4
  print("The oldest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



def my_function(country = "georgia"):  #5
  print("I am from " + country)

my_function("german")
my_function("israel")
my_function()
my_function("asmerima")








