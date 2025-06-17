books_ID = [50,34,-1,-1,2,23,-1]
new_books_ID = []
returned = 0
for _ in range(10):
    id = int(input('books id'))
    books_ID.append(id)
for id in books_ID:
    if id == -1:
        returned += 1
    else:
        new_books_ID.append(id)

print(new_books_ID)
print(returned)
