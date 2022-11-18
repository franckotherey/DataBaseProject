import names
from faker import Faker

faker = Faker()
dir = faker.address()
print(' '.join([x.replace('\n', ' ') for x in dir.split(' ')]))



#print(type(names.get_last_name()))
#nombre = names.get_first_name()
#apellido = names.get_last_name()
#print(nombre)
#print(apellido)


