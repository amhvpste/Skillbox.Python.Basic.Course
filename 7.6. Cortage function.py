names =[
    'Tomas',
    'Lukas',
    'Mantas',
]

ages = [
    20,
    21,
    22,
]

peapole = dict(zip(names, ages));
print(peapole)

peapole_2 = {
    i_name: i_age + 10
    for i_name, i_age in zip(names, ages)
}
print(peapole_2)
