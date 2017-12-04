class Credit(object):
    _credit_body = 1600
    _percent = 0.23
    _months = 6

    @property
    def sum(self):
        return self._credit_body * self._percent + self._credit_body

    @property
    def amount_per_month(self):
        return self.sum / self._months


credit = Credit()
print("Must returned", credit.sum)
print("Must returned per month", credit.amount_per_month)


class Credit(object):
    credit_body = 1600
    percent = 0.23
    months = 6

    @staticmethod
    def sum():
        return Credit.credit_body * Credit.percent + Credit.credit_body

    @staticmethod
    def amount_per_month():
        return Credit.sum() / Credit.months


print("Must returned", Credit.sum())
print("Must returned per month", Credit.amount_per_month())
