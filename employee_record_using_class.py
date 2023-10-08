class EmployeeDetails:
    def __init__(self,emp_id,sal,total_bonus,total_overtime,year):
        self.emp_id=emp_id
        self.sal=sal
        self.total_bonus=total_bonus
        self.total_overtime=total_overtime
        self.year=year
        
    def show(self):
        print(self.emp_id,self.sal,self.total_bonus,self.total_overtime,self.year)

details=[]
while True:
    print("Enter 1 to input employee details.")
    print("Enter 2 to display employee details.")
    ch=int(input("Enter your choice: "))
    if ch==1:
        f=0
        emp_id=int(input("Enter id: "))
        for i in details:
            if i.emp_id==emp_id:
                print("Given Employee id already exists.")
                f=1
                break
        if f!=1:
            sal=int(input("Enter sal: "))
            total_bonus=int(input("Enter bonus: "))
            total_overtime=int(input("Enter overtime(in hr): "))
            year=int(input("Enter year: "))
            a=EmployeeDetails(emp_id,sal,total_bonus,total_overtime,year)
            details.append(a)
    if ch==2:
        f=0
        y=int(input("Details of which year you want to know: "))
        for i in details:
            if i.year==y:
                i.show()
                f=1
        if f==0:
            print("No record found")


