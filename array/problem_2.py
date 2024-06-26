# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heroes = ['spider man','thor','hulk','iron man','captain america']
#1
print('Length of heroes: ', len(heroes))
#2
heroes.append('black panther')
print('Black Panther added to the list')
print(heroes)
#3
heroes.pop(len(heroes) - 1)
heroes.insert(3, 'black panther')
print('Added Black Panther after Hulk')
print(heroes)
#4
heroes[1:3] = ['doctor strange']
print('Heroes removed: ')
print(heroes)
#5
heroes.sort()
print('Sorted list: ')
print(heroes)
