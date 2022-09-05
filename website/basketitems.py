{'2': {'name': 'Auto X - WLC380', 'price': '1000.00', 'quantity': 4}}

dictt = {'2': {'name': 'Auto X - WLC380', 'price': '1000.00', 'quantity': 4}, '1': {'name': 'Auto X - WLC200', 'price': '750.00', 'quantity': 3}}

for i,v in dictt.items():
    print(i,v)
    for b,c in v.items():
        print(b,c)