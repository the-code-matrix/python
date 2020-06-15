#Example1
languages = {'Python': 4098, 'Java': 4139, 'C++': 9234}

#Example2
print(languages)
languages = {'Python': 4098, 'Java': 4139, 'C++': 9234}
languages['C'] = 3224
print(languages)

#Example3
print(languages['Python'])

#Example4
print(languages)
del languages['C++']
print(languages)

#Example5
print('Python' in languages)
print('C++' in languages)

#Example6
print(list(languages))
print(sorted(languages))

#Example7

for k, v in languages.items():
    print(k,v)