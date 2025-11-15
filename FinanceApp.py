from datetime import datetime
import csv

class FinanceAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def FetchData(self):
        full_data = []
        with open(self.filename, newline = '', encoding='utf-8') as f:
            next(f) #ignore first line

            csv_file = csv.reader(f)

            for line in csv_file:
                date, des, amount, cat = line

                full_data.append((
                    datetime.strptime(date, "%Y-%m-%d"),
                    des,
                    float(amount),
                    cat
                ))
        
        return full_data

    def FilterByCategory(self, expenses, category):
        return [cat for cat in expenses if cat[3].lower() == category.lower()]

    def NegativeExpenses(self, expenses):
        return [exp for exp in expenses if exp[2] < 0]

    def ReportExpenses(self):
        data = self.FetchData()
        
        category = set(cat[3] for cat in data) #get each category's names
        costs = []
        for xx in category:
            costs.append(
                sum(map(
                    lambda exp: exp[2],
                    self.FilterByCategory(data, xx)
                )
            ))
        
        return dict(zip(category, costs))

BellaShop = FinanceAnalyzer('transaction.csv')
all_data = BellaShop.FetchData()
print(BellaShop.ReportExpenses())