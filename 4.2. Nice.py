def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_precent = int(input('Підвищення ціни за перший рік: '))
second_precent = int(input('Підвищення ціни за другий рік: '))

prices_first = [get_higher_price(first_precent, i_price) for i_price in prices_now]
prices_second = [get_higher_price(second_precent, i_price) for i_price in prices_first]

print('Сума цін за кожен рік:',
      round(sum(prices_now), 2),
      round(sum(prices_first), 2),
      round(sum(prices_second), 2))
2