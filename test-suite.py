import unittest
import birdyboard
import users

class TestBirdy(unittest.TestCase):
  @classmethod

  def test_setupClass(self):
    self.birdyboard = birdyboard.BirdyBoard()

  def test_user_creation(self):
    # test read/write capabilities
    name = 'Test Name'
    handle = 'Test Handle'
    created_user = users.create_user(name, handle)

    self.assertEqual(created_user.name, 'Test Name')
    self.assertEqual(created_user.handle, 'Test Handle')
    self.assertEqual(len(str(created_user.UID)), 5)

  def test_newUserAdded(self):
    # test on the length of the user object to ensure another one was successfully added
    pass

  def test_newPubMessage(self):
    # test on the length of the public message object to ensure another one was successfully added
    pass

  def test_newPrivMessage(self):
    # test on the length of the private message object to ensure another one was successfully added
    pass

if __name__ == '__main__':
    unittest.main()