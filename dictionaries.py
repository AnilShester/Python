glossary = {
    'concatination': "Adding strings",
    'loop': "iterating over a list",
    'operatos': "Maths operators",
    'data_types': "Types of data",
}

for key, value in glossary.items():
    print(f"{key} means {value}")

rivers = {
    'egypt': "nile",
    'nepal': "bagmati",
    'braizl': "amazon",
}

for key, value in rivers.items():
    print(f"The {value} runs through {key}")

for country in rivers.keys():
    print(country)
for river in rivers.values():
    print(river)

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

names = ["anil", "kritika", "jen", "phil", "ajeep"]

for name in names:
    if name in favorite_languages.keys():
        print(f"{name}, thank you for your poll.")
    else:
        print(f"{name}, Please take the poll as soon as possible.")
