class Student:
    def __init__(self, name, surname, booknum, grades):
        self.name = name
        self.surname = surname
        self.booknum = booknum
        self.grades = grades

    def get_avg(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f'{self.name} {self.surname} {self.booknum} {self.grades}'


class Group:
    def __init__(self, students):
        self.__students = []
        if len(students) <= 20:
            self.__students = students
        else:
            print('More than 20 students')

    def addstud(self, student):
        if type(student) == Student:
            if len(self.__students) < 20:
                self.__students.append(student)
            else:
                print('More than 20 students')
        else:
            print('Not student')

    def delatud(self, student):
        if type(student) == Student:
           if student in self.__students:
               self.__students.remove(student)
           else:
               print('Not such student here')
        else:
            print('Not student')

    def print_top(self):
        if self.__students:
            top_students = sorted(self.__students, key=lambda x: x.get_avg(), reverse=True)[:5]
            print('Top five students:')
            for i in range(len(top_students)):
                print(f'{i + 1}. {top_students[i].name} {top_students[i].surname} - {top_students[i].get_avg()} points')

    def printgroup(self):
        for i in range(len(self.__students)):
            print(self.__students[i])



stud1 = Student('Andrii', 'Zubov', 'TV1122', [5, 4, 5, 5])
stud2 = Student('Danilo', 'Titarenko', 'TU2411', [4, 4, 3, 3])
stud3 = Student('Alex', 'Ataman', 'TV1104', [3, 5, 3, 4])
stud4 = Student('Park', 'Parkkovich', 'TY2114', [5, 5, 3, 4])
stud5 = Student('Vanek', 'Chalov', 'TE01223', [5, 5, 4, 5])
stud6 = Student('yorik', 'bobik', 'TY5342', [4, 3, 4, 4])
stud7 = Student('yorik1', 'bobik', 'TY5342', [4, 3, 4, 4])
stud8 = Student('yorik2', 'bobik', 'TY5342', [4, 3, 4, 4])
stud9 = Student('yorik3', 'bobik', 'TY5342', [4, 3, 4, 4])
stud10 = Student('yorik4', 'bobik', 'TY5342', [4, 3, 4, 4])
stud11 = Student('yorik5', 'bobik', 'TY5342', [4, 3, 4, 4])
stud12 = Student('yorik6', 'bobik', 'TY5342', [4, 3, 4, 4])
stud13 = Student('yorik7', 'bobik', 'TY5342', [4, 3, 4, 4])
stud14 = Student('yorik8', 'bobik', 'TY5342', [4, 3, 4, 4])
stud15 = Student('yorik9', 'bobik', 'TY5342', [4, 3, 4, 4])
stud16 = Student('yorik10', 'bobik', 'TY5342', [4, 3, 4, 4])
stud17 = Student('yorik11', 'bobik', 'TY5342', [4, 3, 4, 4])
stud18 = Student('yorik12', 'bobik', 'TY5342', [4, 3, 4, 4])
stud19 = Student('yorik113', 'bobik', 'TY5342', [4, 3, 4, 4])
stud20 = Student('yorik14', 'bobik', 'TY5342', [4, 3, 4, 4])
stud21 = Student('yorik15', 'bobik', 'TY5342', [4, 3, 4, 4])

group1 = Group([stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10, stud11, stud12, stud13, stud14, stud15, stud16, stud17, stud18])
group1.addstud(stud19)
group1.addstud(stud20)
group1.printgroup()
group1.delatud(stud1)
group1.printgroup()
