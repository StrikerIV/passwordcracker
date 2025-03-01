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

guesses = '{:,}'.format(returned[0])

if returned[1] == "not_found":
    print(
        f'\nUnable to solve password {password}. {guesses} guesses were attempted.\n')
else:
    print(
        f'\nSolved password "{password}" with word(s) & number(s) "{returned[1]}" in {guesses} guesses which took {format(timeE-timeS)} seconds.\n')
