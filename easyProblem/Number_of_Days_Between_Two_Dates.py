class Solution():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def get_days(self, date):
        year, month, day = map(int, date.split("-"))
        result = 0

        for  i in range(1971, year):
            result += 365
            if self.is_leap_year(i):
                result +=1

        for i in range(1, month):
            result += self.months[i]
            if (month == 2 and self.is_leap_year(year)):
                result += 1

        return result + day


    def daysBetweenDates(self, date1, date2):
        return abs(self.get_days(date1) - self.get_days(date2))
