phonebook_dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555",
    "David": "444-444-4444",

}

phonebook_dict[("Eva")] = "222-222-2222"
for i_person in phonebook_dict:
    print(f"{i_person}: {phonebook_dict[i_person]}")

print("Phonebook keys:", phonebook_dict.keys())