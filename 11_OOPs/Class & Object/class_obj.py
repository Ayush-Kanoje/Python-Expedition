#Create a Ticket machine


class Employee:

    dept = "Development"

    def __init__(self, ticketID, ticketStatus, ticketDetail):

        self.ticketID = ticketID
        self.ticketStatus = ticketStatus
        self.ticketDetail = ticketDetail


emp1 = Employee(1,"Medium","Need server checkups")
emp2 = Employee(2,"low","check push in branch feature1")
emp3 = Employee(3,"high","check push in branch feature1")
emp4 = Employee(4,"low","check push in branch feature2")
emp5 = Employee(5,"medium","check push in branch feature3")
emp6 = Employee(6,"medium","check push in branch feature4")

print(emp1.ticketID,emp1.ticketStatus, emp1.ticketDetail,emp1.dept)
print(emp2.ticketID,emp2.ticketStatus, emp2.ticketDetail, emp2.dept)
print(emp4.ticketID,emp4.ticketStatus, emp4.ticketDetail, emp4.dept)
print(emp5.ticketID,emp5.ticketStatus, emp5.ticketDetail, emp5.dept)

print("------------------------------------------------------------------")

emp2.dept = "Junior Dev"
emp2.ticketDetail = "Solved just need verification"

print(emp2.ticketID,emp2.ticketStatus, emp2.ticketDetail, emp2.dept)

print(Employee.dept)


