name= str('JUAN DELA CRUZ')
course= str('COMPUTER SCIENCE')
school= str('UNIVERSITY OF PERPETUAL HELP')

school = (school.lower())
name = (name.lower())

text = "Welcome to {}, {}!"

print(text.format(school, name))