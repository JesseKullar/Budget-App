class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.total_cat = float()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,
                            'description': description})

    def withdraw(self, amount, description=""):
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append({"amount": -amount,
                                'description': description})
            self.total_cat += amount
            return True
        else:
            return False

    def get_balance(self):
        balance = float()
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, destination):
        funds = self.check_funds(amount)
        if funds:
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        """checks the amount of funds available.
            This should be used by functions(withdraw, transfer)"""
        current_balance = self.get_balance()
        if amount > current_balance:
            return False
        else:
            return True

    def __str__(self):
        body = ''
        for i in range(len(self.ledger)):
            body += str(self.ledger[i]['description'][:23]).ljust(23) + \
                    format(self.ledger[i]['amount'], '.2f').rjust(7) + '\n'
        return (str(self.name.center(30, '*'))) + '\n' + body + "Total: " + \
               str(self.get_balance())


def round_down(num, divisor):
    return num - (num % divisor)


def percent_spent(categories):
    percent = []
    total_spent = sum([i.total_cat for i in categories])
    for i in categories:
        percent.append(round_down(i.total_cat * 100 / total_spent, 10))
    return percent


def create_spend_chart(categories):
    title = "Percentage spent by category"
    body = ''
    x_label = ''
    count = 100
    body_height = 11
    percent = percent_spent(categories)
    for i in range(body_height):
        body += '\n'
        body += (str(count) + '| ').rjust(5)
        for j in range(len(categories)):
            if count - (int(percent[j])) > 0:
                body += '   '
            else:
                body += 'o  '
        count -= 10

    body += '\n' + ('-' * ((len(categories) * 3) + 1)).rjust((len(categories) * 3) + 5)

    # for label of x axis
    maxlen = max([len(i.name) for i in categories])
    for i in range(maxlen):
        x_label += '\n'
        x_label += '    '
        for j in categories:

            try:
                x_label += ' ' + j.name[i] + ' '
            except IndexError:
                x_label += "   "
        x_label += " "

    return title + body + x_label.rjust((len(categories) * 3) + 5)
