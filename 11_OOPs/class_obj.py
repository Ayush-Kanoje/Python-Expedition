#Create a Ticket machine

class Ticket:
    company = "Khuranaz"

    def __init__(self,ticket_id,ticket_status):

        self.ticket_id = int(ticket_id)
        self.ticket_status = str(ticket_status)


t1 = Ticket(1, "Opened")
print(t1.ticket_status)

t1.ticket_status = "Closed"
print(t1.ticket_status)