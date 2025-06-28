name=input("What is your name? ")
print(name)
Age=int(input("What is your age? "))
#  Age=input("What is your age? ")   Age=Age+1  TypeError: can only concatenate str (not "int") to str
Age=Age+1
print(f"your age is {Age}")