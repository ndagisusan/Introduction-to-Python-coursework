people = [{'name': 'John', 'age':25}, {'name': 'Sarah', 'age':23}, {'name': 'Lisa', 'age' : 101}]
for person in people:
    name = person['name']
    age = person['age']
    if str(age)[-1]=='1': #convert integer to string, get the last character from the string
        variable_text = 'st'
    elif str(age)[-1]=='2':
        variable_text = 'nd'
    elif str(age)[-1]=='3':
        variable_text = 'rd'
    else:
        variable_text = 'th'

    message = 'Hello ' + name + ', happy ' + str(age) + variable_text + ' birthday!'
    print(message)
