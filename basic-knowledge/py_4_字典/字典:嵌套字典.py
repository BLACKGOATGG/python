
#======================================================
print("\n嵌套字典")
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
# 可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

print("\n在字典中存储列表")
aliens = []
for alienNo in range(30):
    new_alien = {
        'no': alienNo, 
        'color': 'green', 
        'speed': 'slow',
        'points': 5
    }
    aliens.append(new_alien)
print(str(len(aliens)))

for alien in aliens[:5]:
    if alien['color'] == "green" :
        alien['color'] = "yellow"
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow': 
        alien['color'] = 'red' 
        alien['speed'] = 'fast' 
        alien['points'] = 15

for alien in aliens:
    print(alien)


print("\n在列表中存储字典")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print("\n")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'], 'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    if len(languages)>1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages: 
            print("\t" + language.title())
    else :
        print("\n" + name.title() + "'s favorite language is " + languages[0].title())


print("\n在字典中存储字典")
users = { 
    'aeinstein': {
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton', 
    },
    'mcurie': {
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
    },
    '撒大': {
        'first': '撒打算', 
        'last': '撒发生', 
        'location': '阿达撒撒撒打算打算', 
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

