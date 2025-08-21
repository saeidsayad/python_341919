# Ex 1

# sentence = input('Enter a word or a sentnce: ')         # Hello WORLd

# lower = 0
# upper = 0
# space = 0

# for character in sentence:
#     if character.islower():
#         lower += 1
#     elif character.isupper():
#         upper += 1
#     elif character.isspace():
#         space += 1

# print('Uppercases: ', upper)
# print('Lowercases: ', lower)
# print('Spaces: ', space)
# ###############################################

# word = input('Enter a word or a sentnce: ').split()
# pigs = []


# for i in word:
#     new_word = i[1:] + i[0] + 'ay'
#     pigs.append(new_word)


# final = ' '.join(pigs)
# print(final)
# #############################################

# fruit = 'apple banana mango'
# mive = 'banana mango orange'

# new_fr = set(fruit.split())
# new_mv = set(mive.split())

# final = list(new_fr.symmetric_difference(new_mv))

# final_str = ' '.join(final)
# print(final_str)
# ###############################################

# mystr = 'PyNaTive'          # 'yaivePNT'

# lower = ''
# upper = ''

# for i in mystr:
#     if i.islower():
#         lower += i
#     elif i.isupper():
#         upper += i

# final = lower + upper
# print(final)
# ###################################

# s1 = 'Abcdef'             # 'AzbycxdW'
# s2 = 'Wxyz'
# new_s2 = s2[::-1]

# final_str = ''

# for i in range(len(new_s2)):
#     final_str += s1[i] + new_s2[i]

# print(final_str + s1[len(new_s2):])

# #########################################

# str1 = '/*Jon is @developer & musician'
# new_str = ''

# for i in str1:
#     if i.isalpha() or i.isspace():
#         new_str += i

# print(new_str)
# ###########################################

# mystr = 'Saeid25 is Data Scientist50 and AI Expert'
# splitted_str = mystr.split()

# new = []

# for word in splitted_str:
#     if word.isalnum() and not word.isalpha() and not word.isdigit():
#         new.append(word)

# print(' '.join(new))
# ##############################################

# mystr = '/*Jon is @developer & musician'
# new_str = ''

# for i in mystr:
#     if i.isalpha() or i.isspace():
#         new_str += i
#     else:
#         new_str += '#'

# print(new_str)
# #################################################

# import string
# import re


# mystr = '/*Jon is @developer & musician'
# punc = string.punctuation           

# final = re.sub(f'[{punc}]', '#', mystr)
# print(final)
# ####################################################

# number = 10
# age = 20

# new = f'hello. the additionb of {number} and {age} is {number + age}'
# print(new)
# ##############################################

# city = 'Tehran'
# color = 'Red'

# new = '{} is a {} city'.format(city, color)
# print(new)
# ##############################################

# colors = 'Red Green Black White Pink'
# new_cl = colors.split()
# new_cl.sort()
# print(' '.join(new_cl))
# ###############################################

# sent = 'PythonExercisesForClass'

# new = ''

# for i in sent:
#     if i.isupper() and sent.index(i) != 0:
#         new += ' ' + i
#     else:
#         new += i

# print(new)
# ################################################

# import datetime


# date = 'Dec 4 2018 10:07 PM'

# format = '%b %d %Y %H:%M %p'

# final = datetime.datetime.strptime(date, format)
# print(final)
# ###################################################

# students = {}

# while True:
#     print('\n1. Add a New Student')
#     print('2. Update Grades')
#     print('3. Display Students')
#     print('4. Exit\n')

#     choice = input('Choose an option(1-4): ')

#     if choice == '4':
#         break
#     elif choice == '3':
#         print(students)
    
#     elif choice == '1':
#         name = input('\nEnter your name:').title()
#         grade = int(input('Enter Your Grade: '))
#         students[name] = grade
    
#     elif choice == '2':
#         name = input('\nEnter your name:').title()
#         if name in students:
#             new_grade = int(input('Enter Your New Grade: '))
#             students[name] = new_grade
#         else:
#             print('\nYour Name is not in our database!')
    
#     else:
#         print('\nInvalid Option. Try Again')

# ########################################

# students = {}

# while True:
#     print('\n1. Add a New Student')
#     print('2. Update Grades')
#     print('3. Display Students')
#     print('4. Exit\n')

#     choice = input('Choose an option(1-4): ')

#     match choice: 
#         case '4':
#             break

#         case '3':
#             print(students)
        
#         case '1':
#             name = input('\nEnter your name:').title()
#             grade = int(input('Enter Your Grade: '))
#             students[name] = grade

#         case '2':
#             name = input('\nEnter your name:').title()
#             if name in students:
#                 new_grade = int(input('Enter Your New Grade: '))
#                 students[name] = new_grade
#             else:
#                 print('\nYour Name is not in our database!')
        
#         case _:
#             print('\nInvalid Option. Try Again')
# ####################################################

# students = {}
# dars = ['math', 'chem', 'phy']

# while True:
#     print('\n1. Add a New Student')
#     print('2. Update Grades')
#     print('3. Calculate Average for Each Student')
#     print('4. Calculate Average for Specific Subject')
#     print('5. Display Students')
#     print('6. Exit\n')

#     choice = input('Choose an option(1-6): ')

#     if choice == '6':
#         break

#     elif choice == '1':
#         name = input('\nEnter your name:').title()
#         lessons = {}
#         for i in dars:
#             grade = int(input(f"Enter {i}'s Grade: "))
#             lessons[i] = grade

#         students[name] = lessons

#     elif choice == '2':
#         name = input('\nEnter your name:').title()
#         if name in students:
#             lesson_name = input('\nEnter desire lesson to update the grade: ')
#             if lesson_name in dars:
#                 new_grade = int(input('Enter Your New Grade: '))
#                 students[name][lesson_name] = new_grade
#             else:
#                 print('\nInvalid Input...')
#         else:
#             print('\nYour Name is not in our database!')

#     elif choice == '3':
#         name = input('\nEnter your name:').title()
#         if name in students:
#             average = sum(students[name].values()) / len(students[name].values())
#             print(f'\nDear {name}, Your Average is: {average}')
#         else:
#             print('\nYour Name is not in our database!')

#     elif choice == '4':
#         lesson_name = input('\nEnter desire lesson to calculate the average: ')
#         if lesson_name in dars:
#             scores = []
#             for i in students:
#                 scores.append(students[i][lesson_name])
            
#             average = sum(scores) / len(scores)
#             print(f'\nThe Average of {lesson_name} is: {average}')

#         else:
#             print('\nInvalid Input...')

#     elif choice == '5':
#         for k, v in students.items():
#             print(f'{k} ----> ')
#             for i, j in v.items():
#                 print(f'\t{i} ------> {j}')
            
#             print()

#     else:
#         print('\nInvalid Option. Try Again')

# ###################################


