class Product:
    def __init__(self, name='product', price=0, description='', dimensions=[1,1,1]):
        if price < 0:
            raise ValueError
        self.atrs = {
            'price' : price,
            'description' : description,
            'dimensions' : dimensions,
            'name' : name
        }

    def edit(self, name, val):
        if val < 0:
            raise ValueError
        if name in self.atrs:
            self.atrs[name] = val
            print(self.atrs)
        else:
            print('There is no such attribute.')

    def __str__(self):
        return f'{self.atrs["name"]} {self.atrs["price"]} {self.atrs["description"]} {self.atrs["dimensions"]}'

class Customer:
    def __init__(self, name='Customer', surname='', patronymic='', number='XXXXXX'):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.number = number

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic} {self.number}'


class Order:
    def __init__(self, customer, products):
        self.cust = customer
        self.products = products

    def add(self, product):
        if type(product) == Product:
            self.products.append(product)
        else:
            print('You can add only products to order.')

    def delete(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print(f'No such product')

    def cacl(self):
        summary = 0
        for i in range(len(self.products)):
            summary = summary + self.products[i].atrs['price']
        return summary

soldier= Customer('Andrii', 'Volchakov', 'Anatolich', 'NUMBER')
himars = Product('HIMARS', 536000, 'Perfect', [30, 57, 15])
STYGNA = Product('STYGNA', 10000, 'PZRK', [1, 2, 3])
rpg = Product('RPG7', 10000, 'For Tanks', [1, 2, 3])
fv4005 = Product('FV4005', 10000000, 'Tank Destroyer', [12, 25, 10])
fv4005.edit('price', 500000)
new_order = Order(soldier, [himars, STYGNA, rpg])
new_order.add(fv4005)
new_order.delete(himars)
new_order.delete(rpg)
print(new_order.cacl())
print(soldier)
print(STYGNA)