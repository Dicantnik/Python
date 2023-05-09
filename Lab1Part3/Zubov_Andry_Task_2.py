class Time:
    def __init__(self, hour, min, sec):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    @property
    def hour(self):
        return self.__hour

    @property
    def min(self):
        return self.__min

    @property
    def sec(self):
        return self.__sec

    @hour.setter
    def hour(self, val):
        if not isinstance(val, int):
            raise ValueError
        if val <= 0 or val >= 24:
            raise ValueError
        self.__hour = val

    @min.setter
    def min(self, val):
        if not isinstance(val, int):
            raise ValueError
        if val <= 0 or val >= 60:
            raise ValueError
        self.__min = val

    @sec.setter
    def sec(self, val):
        if not isinstance(val, int):
            raise ValueError
        if val <= 0 or val >= 60:
            raise ValueError
        self.__sec = val

    def plh(self):
        if self.__hour == 23:
            self.__hour = 0
            return self.__hour
        else:
            self.__hour += 1
            return self.__hour

    def plm(self):
        if self.__min == 59:
            self.__min = 0
            return self.__min
        else:
            self.__min += 1
            return self.__min

    def pls(self):
        if self.__sec == 59:
            self.__sec = 0
            return self.__sec
        else:
            self.__sec += 1
            return self.__sec




first = Time(12, 34, 59)
print(first.hour)
print(first.min)
print(first.sec)
print(first.pls())
print(first.plm())
print(first.plh())


