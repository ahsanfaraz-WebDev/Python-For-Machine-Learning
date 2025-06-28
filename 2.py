name = "Ahsan Faraz"
gpa=2.9
age =25
is_Student = True
is_Employee = False

if is_Student:
    print(f"{name} is a Student")
else:
    print(f"{name} is not a student")

if is_Employee:
    print(f"{name} is an Employee")
else:
    print(f"{name} is not an Employee")

print(f"My age is {age}")

age+=1
age_string=str(age)
# Example of type conversion
name_bool = bool(name)
print(f"My name as a boolean is {name_bool}")
print(f"My age is {age_string}")
print(type(age_string))
print(type(age))
