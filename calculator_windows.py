# Calculater.py

# Library
import os
import math
from datetime import datetime
from pyfiglet import figlet_format
from termcolor2 import colored


# Clear Terminal
os.system('cls')

# Welcome
print(colored(
    '==================================================================', color='blue'))
print(colored(figlet_format('Welcome'), color='cyan'))
print(colored(
    '==================================================================', color='blue'))
print(colored('Welcome To Moein Calculator', color='cyan'))
print(colored('Start Working With The Calculator', color='white'))
time = datetime.now()
print(f'Your Date Of Use Of The Caculator ===> {time}')
print(colored(
    '==================================================================', color='blue'))

# Try For Program
try:

    # While
    while True:

        # Value Input Option
        user_op = input('''
==================================================
[1]  ===> +
[2]  ===> -
[3]  ===> *
[4]  ===> /
[5]  ===> Power
[6]  ===> Calculate The Factorial Of A Number
[7]  ===> Exit The Program
Enter Option ===> ''')

        # IF
        if user_op == '1':
            print('                                   ')
            number1 = float(input('Enter Number1 ===> '))
            number2 = float(input('Enter Number2 ===> '))
            print('                                ')
            print(f'Answer ===> {number1} + {number2}: {number1+number2}')

        elif user_op == '2':
            print('                                   ')
            number1 = float(input('Enter Number1 ===> '))
            number2 = float(input('Enter Number2 ===> '))
            print('                                ')
            print(f'Answer ===> {number1} - {number2}: {number1-number2}')

        elif user_op == '3':
            print('                                   ')
            number1 = float(input('Enter Number1 ===> '))
            number2 = float(input('Enter Number2 ===> '))
            print('                                ')
            print(f'Answer ===> {number1} * {number2}: {number1*number2}')

        elif user_op == '4':
            print('                                   ')
            number1 = float(input('Enter Number1 ===> '))
            number2 = float(input('Enter Number2 ===> '))
            print('                                 ')
            print(f'Answer ===> {number1} / {number2}: {number1/number2}')

        elif user_op == '5':
            print('                                   ')
            number1 = float(input('Enter Number1 ===> '))
            number2 = float(input('Enter Number2 ===> '))
            print('                                 ')
            print(
                f'Answer ===> {number1} ** {number2}: {number1**number2}')

        elif user_op == '6':
            print('                                   ')
            number = int(input('Enter Number ===> '))
            print('                                 ')
            print(f'Answer ===> {number}!: {math.factorial(number)}')

        elif user_op == '7':
            print('                                    ')
            print(
                colored('=================================================', color='blue'))
            print(colored(figlet_format('Good Luck'), color='cyan'))
            break

        else:
            print('                                    ')
            print(colored('Please Enter The Position Correctly', color='red'))
            continue

# Except For Try
except:
    print(colored('Please Try Again', color='red'))


# Create By Moein Heshmati
# Finish
