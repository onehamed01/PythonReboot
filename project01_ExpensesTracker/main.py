from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d")

expenses = [
    (current_date, 12.40, 'Food', 'ASDA weekly shopping'),
    (current_date, 43.70, 'Internet', 'Vodafone Bill'),
]

if expenses:
    print("Date\tAmount\tCategory\tNote")
    for i in expenses:
        print(*i, sep='\t')