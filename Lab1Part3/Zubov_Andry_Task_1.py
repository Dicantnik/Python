class Person:
    def __init__(self, sur, pas, ed, prof, date, vpref, salpref):
        self.__sur = sur,
        self.__pas = pas,
        self.__educ = ed,
        self.__prof = prof,
        self.__date = date,
        self.__vpref = vpref,
        self.__salpref = salpref

    def changesur(self, val):
        self.__sur = val

    def changepas(self, val):
        self.__pas = val

    def changeeduc(self, val):
        self.__educ = val

    def changeprof(self, val):
        self.__prof = val

    def changdate(self, val):
        self.__date = val

    def changevpref(self, val):
        self.__vpref = val

    def changesalpref(self, val):
        self.__salpref = val

    def __str__(self):
        return f'{self.__sur} {self.__pas} {self.__educ} {self.__prof} {self.__date} {self.__vpref} {self.__salpref}'

class Querry:
    querry = []
    def __init__(self, per):
        if type(per) == Person:
           self.querry.append(per)
        else:
            raise ValueError

    def add(self, per):
        if type(per) == Person:
           self.querry.append(per)
        else:
            raise ValueError

    def delete(self, per):
        if per in self.querry:
            self.querry.remove(per)
        else:
            raise ValueError

    def printstat(self):
        for i in self.querry:
            print(i)

first = Person('Zub', '45765768', 'high', 'Builder', '12.07.1999', 'Builter', '2000$')
second = Person('Zu', '87765768', 'middle', 'Prograsmer', '12.06.2000', 'Senior', '10000000$')
query = Querry(first)
query.add(second)
query.printstat()
first.changesur('efsf')
query.printstat()
