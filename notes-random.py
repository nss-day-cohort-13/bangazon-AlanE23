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