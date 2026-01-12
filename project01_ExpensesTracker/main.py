from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d")

def sample_data():
    expenses = [
        {
        'date':current_date, 
        'amount':30.10,
        'category':'Food', 
        'description':'Asda Weekly shopping'
        },
        {
        'date':current_date,
        'amount':43.70,
        'category':'Bill', 
        'description':'Vodafone Internet'
        },
    ]

    if expenses:
        print('Date\tAmount\tCategory\tNote')
        for el in expenses:
            print(*el.values(), sep='\t')
