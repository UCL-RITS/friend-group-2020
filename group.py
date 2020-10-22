"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# define individual people

liam = {'Name': 'Liam',
        'Age': 22,
        'Job': 'Student (MRes Medical Imaging)',
        'Connections': [['Ed', 'Colleague'],
                        ['Premal', 'Colleague'],
                        ['Wang', 'Colleague']]}

premal = {'Name': 'Premal',
        'Age': 21,
        'Job': 'Student (MSc Astrophysics)',
        'Connections': [['Ed', 'Colleague'],
                        ['Liam', 'Colleague'],
                        ['Wang', 'Colleague']]}

ed = {'Name': 'Ed',
        'Age': 22,
        'Job': 'Student (MSc Scientific Computing)',
        'Connections': [['Liam', 'Colleague'],
                        ['Premal', 'Colleague'],
                        ['Wang', 'Colleague']]}

wang = {'Name': 'Wang',
        'Age': 32,
        'Job': 'Student (MSc Physics and Engineering in Medicine)',
        'Connections': [['Liam', 'Colleague'],
                        ['Premal', 'Colleague'],
                        ['Ed', 'Colleague']]}

morgan = {'Name': 'Morgan',
          'Age': 26,
          'Job': [],
          'Connections': []}

my_group = [liam, premal, ed, wang]
# morgan]

print(my_group)

for i in range(len(my_group)):
    entry = my_group[i]
    print(entry['Name'],' is', str(entry['Age']), ', a(n) ',
            entry['Job'],' and (s)he is ',
            entry['Connections'][0][0],"'s ", entry['Connections'][0][1],
            '.')