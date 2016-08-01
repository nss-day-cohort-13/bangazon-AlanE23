import pickle #to serialize the data (stretch goal, not applicable now)

class Birdyboard:

  def __init__(self):
    pass

  def main_menu(self):

    print('Welcome to Birdyboard')
    print('Are you a...')
    print("1. New User")
    print("2. Existing User")
    print("3. View Public Chirps")
    main_input = input("> ")

    try:
      if int(main_input) > 0 and int(main_input) < 4:

        if main_input == '1':
          # call create new user function
          pass

        if main_input == '2':
          # call function holding the select user menu
          pass

        if main_input == '3':
          # call view public chirps function loading public chirps
          pass

      else:
        print('Please enter 1 for New User, 2 for Existing User, or 3 to view all Public Chirps')

    except:
      pass