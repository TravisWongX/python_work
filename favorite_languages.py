favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")

print(favorite_languages.items())

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages: # keys()方法可以省去，默认调用
    print(name.title())