import re

text = 'AV - Analytical View\n'

result = re.match(r'AV', text)
print('Search in start',result) 
print(result.group(0)) if result else print('No match')
print(result.start(), result.end()) if result else print('No match')


result = re.search(r'Analytical', text)
print('Search in text', result)
print(result.group(0)) if result else print('No match')
print(result.start(), result.end()) if result else print('No match')

result = re.findall(r'\w+', text)
print('Find all words', result)