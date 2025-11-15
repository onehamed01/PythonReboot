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
                    date.datetime.strptime(date, "%Y-%m-%d"),
                    des,
                    float(amount),
                    cat
                ))
        
        return full_data

