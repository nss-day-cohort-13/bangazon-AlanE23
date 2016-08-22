# # Random Notes for the Birdy Board Mastery Exercise

import unittest


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_user_creation(self):
    user = User("Tractor Ryan", "tryan")
    self.assertEqual("Tractor Ryan", user.full_name)
    self.assertEqual("tryan", user.screen_name)
    self.assertIsNotNone(user.user_id)
    self.assertIsInstance(user, User)
    pass



if __name__ == '__main__':
    unittest.main()

###################################
import unittest


class TestConversation(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass




if __name__ == '__main__':
    unittest.main()

##################################
import unittest
import ConversationSingleton


class TestChirp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_reply_public_chirp_creation(self):
    pass


  def test_new_public_chirp_creation(self):
    source = User("Arnold Swartzeneggar", "terminator")
    chirp = Chirp(
                  message="Hi everyone",
                  user=source.user_id,
                  private=False
                  )

    it_exists = ConversationSingleton.chirp_exists_in_conversation(chirp)

    self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "Hi everyone")
    self.assertEqual(chirp.user_id, source.user_id)
    self.assertEqual(chirp.private, False)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)


  def test_private_chirp_creation(self):
    source = User("Arnold Swartzeneggar", "terminator")
    target = User("George Lucas", "hahajarjar")
    chirp = Chirp(
                  message="Hi everyone",
                  user=source.user_id,
                  private=True,
                  receiver=target.user_id
                  )
    self.assertIsInstance(chirp, Chirp)




if __name__ == '__main__':
    unittest.main()

#######################################
#Pickle Usage#
#######################################

import pickle

class Notes:

  def __init__(self):
    self.all_notes = []
    try:
      self.deserialize()
    except FileNotFoundError:
      pass

  def list_notes(self):
    [
      print(str(key) + ": " + note)
      for key,note in enumerate(self.all_notes)
    ]

  def prompt(self):
    note = input('Post your inane opinions here > ')

    if note == 'ls':
      self.list_notes()

    elif note == 'rm':
      self.list_notes()
      deleted = input('Which one? > ')
      del(self.all_notes[int(deleted)])

    elif note != 'quit':
      self.all_notes.append(note)
      self.serialize()

    if note != "quit":
      self.prompt()

  def serialize(self):
    with open('notes.txt', 'wb+') as f:
      pickle.dump(self.all_notes, f)

    with open('notes.txt', 'rb') as f:
      binary = f.read()

  def deserialize(self):
    try:
      with open('notes.txt', 'rb+') as f:
        self.all_notes = pickle.load(f)

    except EOFError:
      pass

    return self.all_notes


# import pickle

# class Notes:

#   def __init__(self):
#     self.all_notes = []
#     try:
#       self.all_notes = self.deserialize()
#     except FileNotFoundError:
#       pass

#   def list_notes(self):
#     [
#       print(str(key) + ": " + note)
#       for key,note in enumerate(self.all_notes)
#     ]

#   def prompt(self):
#     note = input("Enter quick note > ")

#     if note == "ls":
#       self.list_notes()

#     elif note == "rm":
#       self.list_notes()
#       deleted = input("Which one? > ")
#       del(self.all_notes[int(deleted)])

#     elif note != "quit":
#       self.all_notes.append(note)
#       self.serialize()

#     if note != "quit": self.prompt()

#   def serialize(self):
#     with open('notes.txt', 'wb+') as f:
#       pickle.dump(self.all_notes, f)

#     with open('notes.txt', 'rb') as f:
#       binary = f.read()

#     return binary


#   def deserialize(self):
#     try:
#       with open('notes.txt', 'rb+') as f:
#         self.all_notes = pickle.load(f)
#     except EOFError:
#       pass

#     return self.all_notes

def create_customer_menu():

  global menu_display
  global all_users
  menu_display = False

  os.system('cls' if os.name == 'nt' else 'clear')

  print("Enter customer name")
  name = input("> ")

  print("Enter street address")
  address = input("> ")

  print("Enter city")
  city = input("> ")

  print("Enter state")
  state = input("> ")

  print("Enter postal code")
  zipcode = input("> ")

  print("Enter phone number")
  phone = input("> ")

  # Verify is working
  user = User(name, address, city, state, zipcode, phone)
  all_users[user.uuid.__str__()] = user #make this an add users function then serialize it
  print(all_users)
  serialization.serialize_users(all_users)
  # will call function for instantiating new user, to be added later
  cust_create_success(name)

def cust_create_success(name):

  os.system('cls' if os.name == 'nt' else 'clear')

  print("We successfully added {} as a user.\n Press enter to continue.".format(name))
  print("\n")
  input("> ")
  global menu_display
  menu_display = True
  start_menu()


def choose_customer_menu():
  menu_display = False
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Which customer will be active?")
  print("\n")

  temp_user_thing = dict()
  global all_users
  counter = 1
  for key, value in all_users.items():
    print("{}. {}".format(counter, value.name))
    temp_user_thing[counter] = value
    counter += 1

  # need to write statement to handle exceptions
  user_choice = int(input("> "))
  for key, value in temp_user_thing.items():
    if key == user_choice:
      global user_login
      user_login = True
      global current_user
      current_user = value

  start_menu()

    # needs to call the function that pulls the rest of the customer information

def create_pay_opt_menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Enter payment type (e.g. AmEx, Visa, Checking)")
  pay_type = input("> ")

  print("Enter account number")
  account = input("> ")
  # needs to run function to have user payment information added to file that holds that information
  added_pay_opt_success(pay_type)

def added_pay_opt_success(pay_type):
  os.system('cls' if os.name == 'nt' else 'clear')

  print("We successfully added {} as payment method. Press enter to continue.".format(pay_type))
  print("\n")
  input("> ")
  global menu_display
  menu_display = True
  start_menu()