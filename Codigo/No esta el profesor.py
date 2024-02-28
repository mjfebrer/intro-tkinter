# El profesor ha faltado a clase y los alumnos se las quieren areeglar solos.
# Haz que te pida el nombre y edad de cada alumno y que despues te diga quien es el mayoy y quien es el menor ( mayor: profesor y menor: sistente).

number_of_classmates = int(input('How many classmates have assisted today? '))
classmates = []


def ask_for_info():
    name = (input("Introduce your name "))
    age = int(input("Introduce your age "))
    classmates.append({'name': name, 'age': age})


i = 1
for i in range(number_of_classmates):
    ask_for_info()


classmates.sort(key=lambda classmate: classmate['age'])


assistant = classmates[0]

classmates.reverse()

teacher = classmates[0]

print('The teacher is', teacher['name'], 'because he/she is ', teacher['age'], 'years old.')
print('The assistant is', assistant['name'], 'because he/she is ', teacher['age'], 'years old.')

# I need the classmates list to be sorted by age
