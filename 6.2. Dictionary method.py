# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1

#     return sym_dict

# text = input("Enter a string: ").lower()
# hist = histogram(text)

# for i_sim in sorted(hist.keys()):  
#     print(f"{i_sim}: {hist[i_sim]}") 

# print('max value:', max(hist.values()))


contacts_list = [
    {"name": "Іван Петренко", "phone": "+380631234567"},
    {"name": "Олена Коваль", "phone": "+380674112233"},
    {"name": "Андрій Шевченко", "phone": "+380503334455"},
    {"name": "Марія Іванова", "phone": "+380931d5234321"},
    {"name": "Сергій Бондар", "phone": "+3806615112244"}
]


contacts = {
    "Іван Петренко": "+380631234567",
    "Олена Коваль": "+380671112233",
    "Андрій Шевченко": "+380503334455",
    "Марія Іванова": "+380931234321",
    "Сергій Бондар": "+380661112244"
}

# Оновлюємо словник contacts даними зі списку contacts_list
for contact in contacts_list:
    contacts[contact["name"]] = contact["phone"]

# Видаляємо контакт "Марія Іванова" зі словника
contacts.pop("Марія Іванова", None)

print("Словник контактів після оновлення і видалення:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")
