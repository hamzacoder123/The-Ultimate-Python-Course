class Employee: 
    language = "Python" # This is a class attribute
    salary = 200000


harry = Employee()
harry.language = "JavaScript" # This is an instance attribute
print(harry.language, harry.salary)
 
