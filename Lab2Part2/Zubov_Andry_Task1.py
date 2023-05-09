class Organization:
    def __init__(self, name, num, address, num_of_employee):
        self.name = name
        self.num = num
        self.address = address
        self.employee = num_of_employee

    def getname(self):
        return self.name


    def getnum(self):
        return self.num

    def getaddress(self):
        return self.address


    def getemployee(self):
        return self.employee

    def setname(self, val):
        if isinstance(val, str):
            self.name = val
        else:
            raise ValueError

    def setnum(self, val):
        if isinstance(val, str):
            self.num = val
        else:
            raise ValueError

    def setaddress(self, val):
        if isinstance(val, str):
            self.address = val
        else:
            raise ValueError


    def setemployee(self, val):
        if isinstance(val, int):
            self.employee = val
        else:
            raise ValueError


    def __add__(first, second):
        return first.employee + second.employee

    def __sub__(first, second):
        return first.employee - second.employee

class Cathedra(Organization):
    def __init__(self, name, num, address, num_of_employee, specialty, numbak, numspec, nummag):
        super().__init__(name, num, address, num_of_employee)
        self.specialty = specialty
        self.numbak = numbak
        self.numspec = numspec
        self.nummag = nummag

    def getspecialty(self):
        return self.specialty

    def getnumbak(self):
        return self.numbak

    def getnumspec(self):
        return self.numspec

    def getnummag(self):
        return self.nummag

    def setspecialty(self, val):
        if isinstance(val, str):
            self.specialty = val
        else:
            raise ValueError

    def setnumbak(self, val):
        if isinstance(val, int):
            self.numbak = val
        else:
            raise ValueError

    def setnumspec(self, val):
        if isinstance(val, int):
            self.numspec = val
        else:
            raise ValueError

    def setnummag(self, val):
        if isinstance(val, int):
            self.nummag = val
        else:
            raise ValueError

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Phone number: {self.num}\n' \
               f'Address: {self.address}\n' \
               f'Num of employees: {self.employee}\n' \
               f'Specialty: {self.specialty}\n' \
               f'Number Bak: {self.numbak}\n' \
               f'Number Spec: {self.numspec}\n' \
               f'Number Mag: {self.nummag}'

class Faculty:
    def __init__(self, cathedras):
        self.__departments = cathedras

    def adddep(self, faculty):
        self.__departments.append(faculty)

    def numstud(self):
        max_num_stud = 0
        for i in self.__departments:
            max_num_stud += i.numbak
            max_num_stud += i.nummag
            max_num_stud += i.numspec
        return max_num_stud

    def __iter__(self):
        self.n = 0
        for i in self.__departments:
            yield i

    def __next__(self):
        if self.n < len(self.__departments):
            self.n += 1
            return self.__departments[self.n-1]
        else:
            raise StopIteration




num1 = Cathedra('fsefss', 'adahjkg', 'sefsese', 50, 'fesfs', 50, 150, 40)
num2 = Cathedra('fsegrdsgdrss', 'adawwadahjkg', 'srgddgefsese', 50, 'fawdawdesfs', 50, 150, 40)
print(num1)
print(num1 + num2)
print(num1 - num2)
fak1 = Faculty([num1, num2])
print(fak1)
i = iter(fak1)
print(next(i))