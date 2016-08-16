import pickle
from users import *

class Birdyboard:

  def __init__(self):
    pass #deserialize everything here on load of program

  def main_menu(self):

    print('\n')
    print('*********************************')
    print('** ~~~Welcome to Birdyboard~~~ **')
    print('*********************************')
    print('\n')

    print('Enter an Integer Corresponding to an Option Below')
    print('\n')
    print("1. New User")
    print("2. Existing User")
    print("3. View Public Chirps")
    print("4. Exit")
    main_input = input("> ")

    if int(main_input) > 0 and int(main_input) < 5:

      if main_input == '1':

        print('Type your given name')
        name = input('> ')

        print('Type your handle')
        handle = input('> ')

        new_user = User(name, handle)

        self.chirp_menu()

      elif main_input == '2':
        # call function holding the select user menu
        pass

      elif main_input == '3':
        # call view all public chirps function loading public chirps
        pass

      elif main_input == '4':
        exit()

    else:
      print('Please enter 1 for New User, 2 for Existing User, or 3 to view all Public Chirps')
      self.main_menu()

  def chirp_menu(self):

    print('\n')
    print('Select One of the Options Below and Chirp Away')
    print('\n')
    print('1. Create Public Chirp')
    print('2. Reply to a Specific Public Chirp')
    print('3. Create Private Chirp')
    print('4. View All Chirps')
    print('5. Return to the Main Menu')
    print('\n')

    menu_input = input('> ')

    if int(main_input) > 0 and int(main_input) < 5:

      if menu_input == '1':
        print('Chirp Away Publicly')
        message = input('> ')

        create_public_chirp(message)

        self.chirp_menu()

      elif menu_input == '2':
        # reply to public chirp function/menu
        pass

      elif menu_input == '3':
        # private chirp function/menu
        pass

      elif menu_input == '4':
        # view all chirps
        pass

      elif menu_input == '5':
        self.main_menu()

    else:
      print('Please Choose Between Options 1, 2, 3, 4, or 5')
      self.chirp_menu()


