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

# d1 = {'orage': 20, 'apple': 3, 'banana': 2}
# d2 = {'peach': 4, 'banana': 12, 'apple': 9}

# for key in d2:
#     if key not in d1:
#         d1.setdefault(key, d2[key])         # d1[key] = d2[key]
#     else:
#         d1[key] += d2[key]

# print(d1)
# #########################################

# import matplotlib.pyplot as plt


# data = [12, 13, 13, 17, 14, 14, 14, 17,
#         17, 17, 17,
#         18, 18, 18,
#         19, 19,
#         20]


# plt.hist(data, color='red')
# plt.show()
# ############################################

# import random
# from random import randint, randrange
# from random import *
# import statistics as st
# from statistics import correlation as cr
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import seaborn as sns
# from sklearn.neighbors import KNeighborsClassifier as knn
# ##################################################

# data = ['hello', 20, 30, 100, 2999]
# name = ['rose', 'ali', 'sara', 45]

# # ('hello', 'rose'), (20, 'ali'), (30, 'sara')

# result = zip(data, name)

# for i, j in result:
#     print(j)

# data = ['hello', 20, 30, 100, 2999, 30, 25, 30, 40]

# indx = []

# for i, j in enumerate(data):
#     if j == 30:
#         indx.append(i)

# print(indx)
# ###################################

# data = ['ali', 20, 'sara', 20, 'rose', 20, 20, 20, 20, 20, 30, 40]

# for i in data:
#     if i == 20:
#         data.remove(i)

# print(data)
# ######################################

# def show_message():
#     print('We Are in the show function')


# show_message()


# def add_number(x):
#     print(x + 10)


# add_number(12.87)
# #####################

# def sum_num(adad1, adad2):
#     print(adad1 + 10 + adad2)


# sum_num(3, 7)
# ################################

# def add_numbers(first_num, second_num):
#     return first_num + second_num


# data = [10, 20, 30, 40]

# average = add_numbers(10, 50) / 5
# print(average)
# #######################################

# from math import pi


# def area(radius):
#     return pi * radius ** 2

# def perimeter(radius):
#     return 2 * pi * radius

# def salary(working_hours, salary_per_hour):
#     if working_hours > 44:
#         normal = salary_per_hour * 44
#         extra = (working_hours - 44) * 1.5 * salary_per_hour
#         return normal + extra
#     else:
#         return working_hours * salary_per_hour


# user_information = {
#     'David': 10500,
#     'Alex': 32000,
#     'Mary': 24000,
#     'Saeid': salary(56, 3),
#     'Circle': area(10)
# }

# print(user_information)
# #############################################


