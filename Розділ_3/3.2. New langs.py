
langs = ["Python", "C++", "Java"]
user_lang = input("Enter a language: ")
i_lang = langs.index(user_lang)
langs.insert( i_lang + 1,"C++")
print(langs)