class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __gt__(self, other):
        if isinstance(other, Calendar):
            if self.year > other.year:
                return True
            elif self.year == other.year and self.month > other.month:
                return True
            elif self.year == other.year and self.month == other.month and self.day > other.day:
                return True
            else:
                return False
        else:
            raise ValueError

    def __lt__(self, other):
        if isinstance(other, Calendar):
            if self.year < other.year:
                return True
            elif self.year == other.year and self.month < other.month:
                return True
            elif self.year == other.year and self.month == other.month and self.day < other.day:
                return True
            else:
                return False
        else:
            raise ValueError

    def __eq__(self, other):
        if isinstance(other, Calendar):
            if self.year == other.year and self.month == other.month and self.day == other.day:
                return True
            else:
                return False
        else:
            raise ValueError

    def __ge__(self, other):
        if isinstance(other, Calendar):
            return self.__gt__(other) or self.__eq__(other)
        else:
            raise ValueError

    def __le__(self, other):
        if isinstance(other, Calendar):
            return self.__lt__(other) or self.__eq__(other)
        else:
            raise ValueError

    def __iadd__(self, other):
        if isinstance(other, Calendar):
            year = self.year + other.year
            month = self.month + other.month
            day = self.day + other.day
            if self.month == 2:
                if day > 28:
                    month += 1
                    day -= 29
            elif self.month % 2:
                if day > 30:
                    month += 1
                    day -= 32
            else:
                if day > 31:
                    month += 1
                    day -= 32
            if month > 12:
                year += 1
                month -= 12
            return Calendar(year, month, day)
        else:
            raise ValueError

    def __str__(self):
        return f'Years: {self.year}\n' \
               f'Monthes: {self.month}\n' \
               f'Days: {self.day}\n'

    def __isub__(self, other):
        if isinstance(other, Calendar):
            if self.__ge__(other):
                year = self.year - other.year
                month = self.month - other.month
                day = self.day - other.day
                if day < 0:
                    month -= 1
                    if self.month == 3:
                        day = 28 + day
                    elif self.month % 2 == 0:
                        day = 30 + day
                    else:
                        day = 31 + day
                if month < 0:
                    year -= 1
                    month = 12 + month
                return Calendar(year, month, day)
            else:
                raise ValueError('Second date bigger than first')
        else:
            raise ValueError

first = Calendar(2003, 6, 12)
second = Calendar(2005, 7, 4)

print(first > second)
print(first >= second)
print(first < second)
print(first <= second)
print(first == second)









