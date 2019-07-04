class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls,date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(year,month,day)

    @staticmethod
    def is_valid(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year)>0 and int(month)>0 and int(month)<=12 and int(day)>0 and int(day)<=31 :
            return True
        else:
            return False

    def __str__(self):
        return "{}/{}/{}".format(self.year,self.month,self.day)

if __name__ == '__main__':
    date = Date(2019,6,16)
    print(date)

    date_str = "2018-6-16"
    print(Date.is_valid(date_str))
    new_date = Date.from_string(date_str)
    print(new_date)


