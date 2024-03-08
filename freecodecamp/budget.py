class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.__balance = 0.0
        self.__spent = 0.0
    def get_spent(self):
        return self.__spent
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,"description": description})
        self.__balance += amount
    def check_funds(self, amount):
        return self.__balance >= amount
    def withdraw(self, amount, description=""):
        if self.__balance >= amount:
            self.ledger.append({"amount": -1 * amount,"description": description})
            self.__balance -= amount
            self.__spent += amount
            return True
        return False
    def get_balance(self):
        return self.__balance
    def transfer(self, amount, instance):
        if self.withdraw(amount, f'Transfer to {instance.name}'):
            instance.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    def __str__(self):
        title = self.name.center(30, '*')
        body = "".join([f'\n{transaction["description"][:23] : <23}{str(format(transaction["amount"], ".2f"))[:7] : >7}' for transaction in self.ledger])
        footer = f'\nTotal: {str(round(self.get_balance(),2))}'
        return title + body + footer
def create_chart_footer(data):
    max_name_lenth = 0
    footer = '\n' + 4 * ' ' + '-' * (1 + 3* len(data))
    for category in data:
        max_name_lenth = max(max_name_lenth, len(category["name"]))
    names = [list(category["name"] + " " * (max_name_lenth - len(category["name"]))) for category in data]
    for i in range(max_name_lenth):
        footer += '\n' + 5 * ' '
        for j in range(len(names)):
            footer += names[j][i] + 2 * ' '
    return footer
def create_chart_body(data):
    graph = []
    percentage_graph = [list('o' * (category["percentage"] + 1) + ' ' * (10 - category["percentage"]))[::-1] for category in data]
    for i in range(11):
        line = [' ']
        for j in range(len(data)):
            line.append(percentage_graph[j][i])
            line.append(' ')
            line.append(' ')
        graph.append(line)
    body = "\n".join([f'{(10 - index) * 10 : >3}|' + ''.join(line) for index, line in enumerate(graph)])
    
    return body
    
def create_spend_chart(categories):
    sum_spent = 0
    data = []
    for category in categories:
        sum_spent += category.get_spent()
    for category in categories:
        percentage = int(category.get_spent() * 10 / sum_spent)
        data.append({
            "name": category.name,
            "percentage": percentage
        })
    header = f'Percentage spent by category\n'
    body = create_chart_body(data)
    footer = create_chart_footer(data)
    graph = header + body + footer
    return graph


food = Category("Food")
food.deposit(100, "initial deposit")
food.withdraw(60, "food 1")

clothing = Category("Clothing")
clothing.deposit(100, "initial")
clothing.withdraw(20, "Ok")
auto = Category("Auto")
auto.deposit(100, "initial")
auto.withdraw(10, "ok")


categories = []
categories.append(food)
categories.append(clothing)
categories.append(auto)

create_spend_chart(categories)