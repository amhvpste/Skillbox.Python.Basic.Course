goods = {
    "Player 1": 54,
    "Player 2": 67,
    "Player 3": 89,
    "Player 4": 45,
    "Player 5": 78,
    "Player 6": 90,
    "Player 7": 100,
    "Player 8": 23,
    "Player 9": 56,
    "Player 10": 88
}

store = {
    '12345': [
        {'quantity': 10, 'price': 5.99},
        {'quantity': 2, 'price': 3.49},
        {'quantity': 2, 'price': 3.49}
    ],
    '67890': [{'quantity': 5, 'price': 12.99}],
    '54321': [{'quantity': 2, 'price': 3.49}],
    '09876': [{'quantity': 8, 'price': 7.99}],
    '11223': [{'quantity': 15, 'price': 9.99}]
}

for i_title, i_code in goods.items():
    total_quantity = 0
    total_price = 0
    for j_good in store[i_code]:
        total_quantity += j_good['quantity']
        total_price += j_good['quantity'] * j_good['price']
    print(f"{i_title} - Total Quantity: {total_quantity}, Total Price: ${total_price:.2f}")
# Example usage