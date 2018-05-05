# Print year which you turn 100 years!

name = input("Enter name :")
age = int(input("Enter your age {}:".format(name)))
n = int(input("Enter the no of copies you want to make:"))
year = str((2018-age)+100)
final = "Hi {}, you will be 100 years by the {} year\n".format(name,year)
print(n*final)
