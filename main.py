#! /usr/bin/env python3
birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)
    
def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

import argparse
#from mypackage.birthdays import return_birthday
parser = argparse.ArgumentParser(description='program that gives back birthdays of scientists')
#define arguments
parser.add_argument("", help= "list of names")
parser.add_argument("--name", help= "insert one of the scientist name of the list")
args = parser.parse_args()
risultato1 = print_birthdays(args.name)
risultato1 = return_birthday(args.name)




