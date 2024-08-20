class Employee :
   
    def __init__(self,name ,salary,extra_hours=50) :
        self.name =  name
        self.salary = salary
        self.extra_hours = extra_hours
    def display(self):
        return display(self.salary)


name:str = str(input("Enter name : "))  
salary:int = int(input("Enter the salary : "))
  
