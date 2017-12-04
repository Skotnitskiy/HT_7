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


class Calculator(object):
    results = []

    @staticmethod
    def add(a, b):
        Calculator.results.append({str(a) + " + " + str(b): a + b})

    @staticmethod
    def subtract(a, b):
        Calculator.results.append({str(a) + " - " + str(b): a - b})

    @staticmethod
    def multiply(a, b):
        Calculator.results.append({str(a) + " * " + str(b): a * b})

    @staticmethod
    def divide(a, b):
        try:
            Calculator.results.append({str(a) + " / " + str(b): a / b})
        except ZeroDivisionError:
            Calculator.results.append({str(a) + " / " + str(b): "Zero division error!"})
            print("Zero division error!")

    @staticmethod
    def get_all_results():
        for result in Calculator.results:
            for operation, res in zip(result.keys(), result.values()):
                print(operation, "=", res)

    @staticmethod
    def get_results(amount):
        if amount < len(Calculator.results):
            for i in range(amount):
                result = Calculator.results[i]
                for operation, res in zip(result.keys(), result.values()):
                    print(operation, "=", res)

    @staticmethod
    def get_previous_result():
        result = Calculator.results[len(Calculator.results) - 2]
        for operation, res in zip(result.keys(), result.values()):
            print(operation, "=", res)


Calculator.add(3, 2)
Calculator.subtract(3, 2)
Calculator.multiply(3, 7)
Calculator.divide(7, 0)
Calculator.get_all_results()
Calculator.get_previous_result()
Calculator.get_results(2)
