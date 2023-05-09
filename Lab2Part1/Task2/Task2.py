import json
from datetime import datetime
import uuid

pizzas = {}

def initpizza(cls):
    pizzas[cls.name] = cls
    return cls


class Pizza:
    def __init__(self):
        self.contains = {
            'dough': 1,
            'cheese': 1,
            'sauce': 1,
            'onion': 1
        }
    def price(self):
        price = 0
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)

            for i in file_data["Ingridients"]:
                if i in self.contains:
                    price += self.contains[i] * file_data["Ingridients"][i]["Price"]
                else:
                    pass
        return price

    def addsmth(self, ingridient):
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            if ingridient in file_data['Ingridients']:
                if ingridient in self.contains:
                    self.contains[ingridient] +=1
                else:
                    self.contains[ingridient] = 1
            else:
                raise ValueError('No such ingridient')


    def __str__(self):
        return f'Pizza contains:\n' \
               f'{self.contains}'


@initpizza
class Monday(Pizza):
    name = 'Monday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["pineapple"]["name"]] = 1


@initpizza
class Tuesday(Pizza):
    name = 'Tuesday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["sausage"]["name"]] = 1

@initpizza
class Wednesday(Pizza):
    name = 'Wednesday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["bellpepper"]["name"]] = 1

@initpizza
class Thursday(Pizza):
    name = 'Thursday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["cucumber"]["name"]] = 1

@initpizza
class Friday(Pizza):
    name = 'Friday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["corn"]["name"]] = 1

@initpizza
class Saturday(Pizza):
    name = 'Saturday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["meat"]["name"]] = 1

@initpizza
class Sunday(Pizza):
    name = 'Sunday'
    def __init__(self):
        super().__init__()
        with open('Ingridients.json', 'r') as file:
            file_data = json.load(file)
            self.contains[file_data['Ingridients']["rusnia"]["name"]] = 1


class Service():
    def purchase(self):
        self.id = uuid.uuid4()
        cur_day = datetime.now()
        cur_day = cur_day.weekday() + 1
        current_pizza = createpizza(cur_day, pizzas_in_file)
        first_pizza = current_pizza()
        print(first_pizza)
        answer = 1
        while (answer):
            answer = input("Add additional ingridient(skip if not)\n")
            if answer:
                first_pizza.addsmth(answer)
                print(first_pizza)
        with open('Pizzas.json', 'r+') as file:
            file_data = json.load(file)
            file_data["Orders"][str(self.id)] = {
                "Name": first_pizza.name,
                "Price": first_pizza.price(),
                "Date": str(datetime.now())
            }
            file.seek(0)
            json.dump(file_data, file, indent=2)
            print("Thanks for purchaising")

    def Info_by_id(self, id):
        with open('Pizzas.json', 'r+') as file:
            file_data = json.load(file)
            for i in file_data["Orders"]:
               if i == id:
                   return file_data["Orders"][i]
            raise ValueError('Not such UID')

def createpizza(day, pizzas1):
    pizza_name = pizzas1[day]
    return pizzas[pizza_name]


pizzas_in_file = {}
with open('Events.txt', 'r') as file:
    for line in file:
        day, name = line.split('.')
        pizzas_in_file[int(day)] = name.strip()

serv = Service()
serv.purchase()
print(serv.Info_by_id("3afeabe7-12b2-4283-b9c6-c1d3b4b96774"))
