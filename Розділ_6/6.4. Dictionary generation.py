data = [
    {'id': 101, 'user': 'bob'},
    {'id': 102, 'user': 'alice'},
    {'id': 103, 'user': 'john'}
]

for record in data:
    print(f"id: {record['id']}, user: {record['user']}")


unique_data = []
for i_dict in data:
    data_exists = False
for unique_dict in unique_data:
    if unique_dict['id'] == i_dict['id']:
        data_exists = True
        break
    if not data_exists:
        unique_data.append(i_dict)
print("\nУнікальні записи:")   

