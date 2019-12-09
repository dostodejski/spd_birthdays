#! /usr/bin/env python3

import argparse
from mypackage.birthdays import return_birthday
parser = argparse.ArgumentParser(description='These are the birthdays of famous people')
#define arguments
parser.add_argument('name', help='it is his birthday', type=str)
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
#parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
args = parser.parse_args()
answer=args.return_birthdays('name')
#return_birthday('Ada Lovelace')


