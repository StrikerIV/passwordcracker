# a213_pw_analyzer.py
import re
import time
import locale
import pwalgorithms as pwa

password = str(input("Enter password to crack: ")).lower()
locale.setlocale(locale.LC_ALL, 'en_US')

timeS = time.time()
returned = pwa.crack_password(password)
timeE = time.time()

print(returned)
guesses = '{:,}'.format(returned[0])

print(f'Solved password "{password}" with word(s) & number(s) "{returned[1]}" in {guesses} guesses which took {format(timeE-timeS)} seconds.')
