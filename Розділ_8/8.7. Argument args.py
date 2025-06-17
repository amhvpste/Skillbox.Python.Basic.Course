def print_tax_document(taxm, *args, **kwargt):
    price_sum = 0
    for i_price in args:
        price_sum += i_price * (1 + taxm / 100)
    
    print('Сума після податків:', round(price_sum, 2))

    for i_info, i_value in kwargt.items():
        print('{}: {}'.format(i_info, i_value))

my_tax = int(input('Податок: '))
print_tax_document(my_tax, 1000, 950, 880, 920, 990, year=1997, doc_type='Report', operation=1111)
