student = {"name": "sita", "age" : 20, "marks": 60}
for key, value in student.items():
     print(key, ",", value)
name = "sita"
city = "delhi"
name = "sita"
text = "Learning Python is Fun"
print(text.upper())
print(text.lower())
print(len(text))
print(text.replace("fun", "awesome"))
print(text[0:8])
print("NEW CODE RUNING")
text = "Python Programming"
print(text.count("m"))
print(text.find("pro"))
print(text.endswith("ing"))
print(text.split())
def calculate_tax(income):
     if income <= 250000:
         tax = 0
     elif income <= 500000:
         tax = (income - 250000) * 0.05
     elif income <= 1000000:
         tax = (250000 * 0.05) + (income - 500000) * 0.2
     else:
         tax = (250000 * 0.05) + (500000 * 0.02) + (income - 1000000) * 0.3
     return tax
annual_income = int(input("enter your annual income: "))
tax = calculate_tax(annual_income)
net_income = annual_income - tax
print("Annual Income:", annual_income)
print("tax:", tax)
print("Net income:", net_income)





