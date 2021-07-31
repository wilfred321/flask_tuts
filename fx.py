# with open('notes.txt','a+') as notes:
#     names = ['Wilfred','Timoth','Getrude','Angela']
#     for name in names:
#         notes.write(f'\n My name is {name}')

class Employee():
    def __init__(self,name,email,salary,job_desc):
        self.name = name
        self.email = email
        self.salary = salary
        self.job_desc = job_desc


    
def register():
    
    name = input("Enter your name:")
    email = input("Enter your email")
    salary = input("How much do you earn?:")
    job_desc = input("Enter your job description:")

    return("{},{},{},{}".format(name,email,salary,job_desc))



# employee1 = Employee('wilfred','owobuwilfred@gmail.com','344003','software engineer')
employee1 = Employee(register())
print(employee1)