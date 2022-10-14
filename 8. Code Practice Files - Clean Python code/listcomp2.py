# List Comprehension Example 2

people_dict_list = [{'name': 'John', 'age':25}, {'name': 'Sarah', 'age':23}, {'name': 'Lisa', 'age' : 101}]

# Print the people's names in a list
# Without list comprehension: FOR LOOP
names = []
for person in people_dict_list:
    names.append(person['name'])

print(names)

# Using LIST COMPREHENSION
names = [person['name'] for person in people_dict_list]
print(names)