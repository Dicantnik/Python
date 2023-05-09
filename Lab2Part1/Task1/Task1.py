from datetime import datetime, date
import uuid
import json


class Ticket:
    def __init__(self, price):
        self.price = price
        self.id = uuid.uuid4()

    def price(self):
        return self.price

    def __str__(self):
        return f'Num: {self.id}, Price: {self.price}'


class Reg_Ticket(Ticket):
    def __init__(self, price, discount):
        super().__init__( price)
        self.price = self.price * (1 - discount)


class Adv_Ticket(Ticket):
    def __init__(self, price, discount):
        super().__init__(price)
        self.price = self.price * (1 - discount)


class Late_Ticket(Ticket):
    def __init__(self, price, discount):
        super().__init__(price)
        self.price = self.price * (1 - discount)


class Stud_Ticket(Ticket):
    def __init__(self, price, discount):
        super().__init__(price)
        self.price = self.price * (1 - discount)


class Service:
    ticket = None
    event = None

    def diftime(self, name):
        with open('package.json', 'r+') as file:
            file_data = json.load(file)
            event_data = file_data['Event'][name]['Date'].split('.')
            now = datetime.now()
            return abs((date(now.year, now.month, now.day) - date(int(event_data[2]), int(event_data[1]), int(event_data[0]))).days)

    def choosing(self):
        with open('package.json', 'r+') as file:
            data_file = json.load(file)
            for i in data_file["Event"]:
                print(i)
            event = input("Choose the Event\n")
            if event not in (data_file["Event"]):
                raise ValueError
            elif data_file["Event"][event]["Tickets"] < 1:
                raise ValueError('No tickets')
            return event

    def Order(self):
        event = self.choosing()
        ticket_type = input("Choose the ticket: Regular / Advanced / Late / Student\n")
        with open('package.json', 'r+') as file:
            data_file = json.load(file)
            if ticket_type == 'Regular':
                ticket = Reg_Ticket(data_file["Event"][event]["Price"], 0)
            elif ticket_type == 'Advanced':
                if self.diftime(event) >= 60:
                    ticket = Adv_Ticket(data_file["Event"][event]["Price"], 0.4)
                else:
                    raise ValueError('Too late')
            elif ticket_type == 'Late':
                if 0 <= self.diftime(event) <= 10:
                    ticket = Late_Ticket(data_file["Event"][event]["Price"], -0.1)
                else:
                    raise ValueError('Too late')
            elif ticket_type == 'Student':
                ticket = Stud_Ticket(data_file["Event"][event]["Price"], 0.5)
            else:
                raise ValueError('Not such ticket')
            data_file["Event"][event]["Tickets"] -= 1
            file.seek(0)
            json.dump(data_file, file, indent=2)
            data = {
                "Uid": str(ticket.id),
                "Price": ticket.price,
                "Date": str(datetime.now()),
                "Type": ticket_type,
                "Event": event
            }
            with open('Tickets.json', 'r+') as file:
                file_data = json.load(file)
                file_data["Tickets"].append(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)

    def Info_by_id(self, id):
        with open('Tickets.json', 'r+') as file:
            file_data = json.load(file)
            for i in range(len(file_data["Tickets"])):
               if file_data["Tickets"][i]["Uid"] == id:
                   return file_data["Tickets"][i]
            raise ValueError('Not such UID')

    def Info_by_NameOfEvent(self, name):
        with open('package.json', 'r+') as file:
            file_data = json.load(file)
            for i in file_data["Event"]:
                if i == name:
                    return file_data["Event"][name]
            raise ValueError('Not such Event')


ter = Service()
ter.Order()
