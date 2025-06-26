import re


text = 'AV is largest Analytics commynity of India\n'

result = re.findall(r'\b[aeiouAEIUO]\w+', text)
print('Find all words', result)