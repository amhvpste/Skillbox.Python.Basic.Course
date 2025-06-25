def fi():
    print("This is a function in the module 'fi'.", number)

def f2():
    number = 50
    print("This is a function in the module 'f2'.", number)

def f3():
    def f5():
        number = 30
        print("This is a function inside f3 -> f5. Number:", number)
    f5()  # Викликаємо внутрішню функцію

number = 100
print("This is a module 'f2'.", number)

# Викликаємо існуючу функцію
fi()

# Викликаємо функцію з локальною змінною
f2()

# Викликаємо f3, яка містить вкладену функцію f5
f3()
