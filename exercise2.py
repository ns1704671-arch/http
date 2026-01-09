students ={ "Pawan": 70,
           "Mani" : 85,
           "akshay": 90,
           "ravi": 55,
           "kirti": 45,
           "geeta": 40,
}
print("students with pass marks:")
for name, marks in students.items():
  if marks >=40:
     print(f"{name}: marks = {marks}")
a = 10
b = 20
c =30
average = (a +b +c) / 3
print("average +", average)
a = 5
b = 10
c = 15 
d = 20
average = (a + b + c +d) / 4
print(average)
def my_function():
    x = 10
    print(x)
my_function()
y = 20
def my_function():
     print(y)
my_function()
print(y)
z = 5
def change():
    global z
    z = 15
change()
print(z)
x = 10
def show():
    x = 5
    print("inside function:", x)
show()
print("outside function:", x)
y = 100
def test():
    print(y)
test()
a = 10
def change():
    global a
    a = 50
change()
print(a)


        