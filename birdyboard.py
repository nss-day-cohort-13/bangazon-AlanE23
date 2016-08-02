# import pickle # to serialize the data (stretch goal, not applicable now)
import csv
import sys
from users import *

class Birdyboard:

  def __init__(self):
    pass

  def main_menu(self):

    print('\n')
    print('***************************')
    print('** Welcome to Birdyboard **')
    print('***************************')
    print('\n')

    print('Enter an Integer Corresponding to an Option Below')
    print('\n')
    print("1. New User")
    print("2. Existing User")
    print("3. View Public Chirps")
    main_input = input("> ")

    try:
      if int(main_input) > 0 and int(main_input) < 4:

        if main_input == '1':

          print('Type your given name')
          name = input('> ')

          print('Type your handle')
          handle = input('> ')

          create_user(name, handle)

        if main_input == '2':
          # call function holding the select user menu
          pass

        if main_input == '3':
          # call view public chirps function loading public chirps
          pass

      else:
        print('Please enter 1 for New User, 2 for Existing User, or 3 to view all Public Chirps')
        self.main_menu()

    except:
      pass