import pickle
import serialize
from users import *
from chirp import *

user_list = {}
chirp_list = {}

current_user = None

def app_start():

  global user_list
  user_list = serialize.deserialize('users.txt', user_list)

  global chirp_list
  chirp_list = serialize.deserialize('chirps.txt', chirp_list)
  print(chirp_list)

  main_menu()

def main_menu():
  global user_list
  global current_user

  print('\n')
  print('*********************************')
  print('** ~~~Welcome to Birdyboard~~~ **')
  print('*********************************')
  print('\n')

  try:
    print("Currently Logged in as: ", current_user.handle)
    print('\n')
  except:
    print('Sign up or choose a user to chirp away')
    print('\n')

  print('Enter an Integer Corresponding to an Option Below')
  print('\n')
  print("1. New User")
  print("2. Existing User")
  print("3. View Public Chirps")
  print("4. Create Chirp")
  print("5. Exit")
  main_input = input("> ")

  if int(main_input) > 0 and int(main_input) < 6:

    if main_input == '1':

      print('Type your given name')
      name = input('> ')

      print('Type your handle')
      handle = input('> ')

      user = User(name, handle)
      user_list[int(user.user_ID)] = user
      print(user_list)
      serialize.serialize('users.txt', user_list)

      main_menu()

    elif main_input == '2':
      # call function holding the select user menu
      print('Select a user')
      print("\n")

      temp_user_list = dict()
      counter = 1
      for key, value in user_list.items():
        print("{}. {}".format(counter, value.handle))
        temp_user_list[counter] = value
        counter += 1

      user_choice = int(input("> "))
      for key, value in temp_user_list.items():
        if key == user_choice:
          current_user = value

      main_menu()

    elif main_input == '3':
      # call view all public chirps function loading public chirps
      print('\n')
      print("Behold all of the mind bending chirps, peasant")
      print('\n')



      ticker = 1
      for key, value in chirp_list.items():
        print("{}. {}".format(ticker, value.message))

      main_menu()

    elif main_input == '4':
      print('Chirp away')

      user_input = input('> ')

      chirp = Chirp(current_user, user_input)
      chirp_list[int(chirp.chirp_ID)] = chirp

      print(chirp_list)
      serialize.serialize('chirps.txt', chirp_list)

      main_menu()

    elif main_input == '5':
      exit()

  else:
    print('Please select a valid option')
    main_menu()

app_start()


















